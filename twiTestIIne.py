import tweepy
import datetime
import json

# 2. JSONファイルを読み込む
jsonFile = open('./config.json', 'r', encoding="utf-8")

# 4. json.load() でJSON文字列をパース(decode)する => JSON文字列を読み込む
parseData = json.load(jsonFile)

# Twitter APIの認証情報を設定
consumer_key=parseData['API_KEY']
consumer_secret=parseData['API_SECRET']
access_token=parseData['ACCESS_TOKEN']
access_token_secret=parseData['ACCESS_TOKEN_SECRET']

# Tweepyクライアントの初期化
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 特定のユーザーのツイートを取得
user_id = 'unixtower2nd'  # 対象ユーザーのID
current_year = datetime.datetime.now().year
start_date = datetime.datetime(current_year, 1, 1)
end_date = datetime.datetime(current_year + 1, 1, 1)

tweets = tweepy.Cursor(api.user_timeline, id=user_id, since=start_date, until=end_date).items()

# いいねの件数を集計
like_counts = []
for tweet in tweets:
    like_counts.append((tweet.text, tweet.favorite_count))

# いいねの件数でソートして上位10件を表示
like_counts.sort(key=lambda x: x[1], reverse=True)
top_10_likes = like_counts[:10]

for tweet, count in top_10_likes:
    print(f'Likes: {count} - Tweet: {tweet}')
