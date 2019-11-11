import requests
import datetime
import tweepy

def getTransactions():
    # get the time in utc timestamp and make it an int not a float
    ends = datetime.datetime.utcnow().timestamp()
    ends = int(ends)

    # take the valid start and end time
    starts = ends - 26000
    end = starts + 3600

    # turn them into a string
    start = str(starts)
    end = str(end)

    # get api from blockchain
    response = requests.get(('https://api.whale-alert.io/v1/transactions?api_key=KtE5Gw2adzR9RT0SX8TGuF2e0k72Y1mq&min_value=1000000&start='+start+'&end='+end+'&cursor=2bc7e46-2bc7e46-5c66c0a7'))
    json_r = response.json()

    # get how many transaction within that certain time frame
    count = json_r["count"]
    
    # if the count is not zero then get the transactions
    if(count != 0):
        transactions = json_r['transactions']
        
        for key in transactions:
            if key['amount_usd'] >= 10000000:
                if key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'exchange':
                    if key['from']['owner'] == key['to']['owner']:
                        twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered on #' + key['from']['owner'].title())
                    else:
                        twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'unknown':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to ' + key['to']['owner_type'])
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'exchange':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'unknown':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to ' + key['to']['owner_type'])
            else:
                if key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'exchange':
                    if key['from']['owner'] == key['to']['owner']:
                        twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered on #' + key['from']['owner'].title())
                    else:
                        twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'unknown':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to ' + key['to']['owner_type'])
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'exchange':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'unknown':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to ' + key['to']['owner_type'])

def twitter(post):
    # all the keys we need for our twitter bot
    CONSUMER_KEY = 'deE16vcPAilCdnc3m7t77Q8TA'
    CONSUMER_SECRET = 'KMIevjvdIcHc94uDrna7DOzJaaGCfl04l9Da6c1TBZuAVyfGG2'
    ACCESS_KEY = '1174927237704871936-4oFhJuMVOvuWs2Qjdwt24PqKA4KIr4'
    ACCESS_SECRET = 'rj5AnNEMUrlQlbfOer8aLDQJsbCvpVAcc8cXL7CQ8sAL1'

    # talk to twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(post)

def main():
    getTransactions()
    
    
main()