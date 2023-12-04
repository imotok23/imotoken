import tweepy
import json

# 認証に必要なキーとトークン

# 2. JSONファイルを読み込む
jsonFile = open('./config.json', 'r', encoding="utf-8")

# 4. json.load() でJSON文字列をパース(decode)する => JSON文字列を読み込む
parseData = json.load(jsonFile)

#データ取得
api_key=parseData['API_KEY']
api_secret=parseData['API_SECRET']
access_token=parseData['ACCESS_TOKEN']
access_token_secret=parseData['ACCESS_TOKEN_SECRET']

# APIの認証
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

client = tweepy.Client(
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_token_secret)

client.create_tweet(text="Hello world!!")
