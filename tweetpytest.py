#ライブラリのインポート
import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd
import json

# 2. JSONファイルを読み込む
jsonFile = open('./config.json', 'r', encoding="utf-8")

# 4. json.load() でJSON文字列をパース(decode)する => JSON文字列を読み込む
parseData = json.load(jsonFile)

#Twitterの認証
#データ取得
api_key=parseData['API_KEY']
api_secret=parseData['API_SECRET']
access_key=parseData['ACCESS_TOKEN']
access_secret=parseData['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)
#検索条件の設定
searchkey = '全然違うじゃん'
item_num = 10
#検索条件を元にツイートを抽出
tweets = tweepy.Cursor(api.search_tweets,q=searchkey,lang='ja').items(item_num)
#関数:　UTCをJSTに変換する
def change_time_JST(u_time):
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    # 文字列で返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time
#抽出したデータから必要な情報を取り出す
#取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
tweet_data = []
for tweet in tweets:
    #ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
    tweet_time = change_time_JST(tweet.created_at)
    create_account_time = change_time_JST(tweet.user.created_at)
    #tweet_dataの配列に取得したい情報を入れていく
    tweet_data.append([
        tweet.id,
        tweet_time,
        tweet.text,
        tweet.favorite_count, 
        tweet.retweet_count, 
        tweet.user.id, 
        tweet.user.screen_name,
        tweet.user.name,
        tweet.user.description,
        tweet.user.friends_count,
        tweet.user.followers_count,
        create_account_time,
        tweet.user.following,
        tweet.user.profile_image_url,
        tweet.user.profile_background_image_url,
        tweet.user.url
                       ])
#取り出したデータをpandasのDataFrameに変換
#CSVファイルに出力するときの列の名前を定義
labels=[
    'ツイートID',
    'ツイート時刻',
    'ツイート内容',
    'いいね数',
    'リツイート数',
    'ID',
    'ユーザID',
    'アカウント名',
    '自己紹介文',
    'フォロー数',
    'フォロワー数',
    'アカウント作成日時',
    '自分がフォローしているか？',
    'アイコン画像URL',
    'ヘッダー画像URL',
    'WEBサイト'
    ]
#tweet_dataのリストをpandasのDataFrameに変換
df = pd.DataFrame(tweet_data,columns=labels)
#CSVファイルに出力する
#CSVファイルの名前を決める
file_name='tweet_data.csv'
#CSVファイルを出力する
df.to_csv(file_name,encoding='utf-8-sig',index=False)
