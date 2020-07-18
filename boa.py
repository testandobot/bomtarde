import os
import tweepy
import time
import datetime
from os import environ

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

frase = ""
def Mensagem(frase):
    for tweet in tweepy.Cursor(api.friends, screen_name = "testandobot007").items():
     try:
         if tweet.screen_name != "SFCAlvinegro" and tweet.screen_name != "VilaSantastica":
             api.update_status(frase + " @" + tweet.screen_name)
         print(tweet.screen_name)
     except tweepy.TweepError as e:
         print(e.reason)
     except StopIteration:
         break

def tweet_check(twitter_checked=True):
    minutos = datetime.datetime.now().minute
    horas = datetime.datetime.now().hour
    if  horas == 11 and minutos == 30:
        Mensagem("Bom dia")
        time.sleep(60)
    if  horas == 16 and minutos == 30:
        Mensagem("Boa tarde")
        time.sleep(60)
    if  horas == 23 and minutos == 30:
        Mensagem("Boa noite")
        time.sleep(60)
    if horas == 16 and minutos == 45:
        print("tá")    
        
if __name__ == '__main__':
    while True:
        tweet_check()
        
     
