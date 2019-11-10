import requests
import datetime
import tweepy

def getTransactions():
    ends = datetime.datetime.utcnow().timestamp()
    ends = int(ends)

    starts = ends - 26000
    end = starts + 3600

    start = str(starts)
    end = str(end)

    response = requests.get(('https://api.whale-alert.io/v1/transactions?api_key=KtE5Gw2adzR9RT0SX8TGuF2e0k72Y1mq&min_value=1000000&start='+start+'&end='+end+'&cursor=2bc7e46-2bc7e46-5c66c0a7'))
    json_r = response.json()

    count = json_r["count"]
    print(count)
    if(count != 0):
        transactions = json_r['transactions']
        print(transactions)

def twitter():
    CONSUMER_KEY = 'AAAAAA'
    CONSUMER_SECRET = 'BBBBBB'
    ACCESS_KEY = 'CCCCCC'
    ACCESS_SECRET = 'DDDDDD'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

def main():
    getTransactions()
    
main()