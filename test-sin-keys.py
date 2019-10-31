import tweepy
import json

consumer_key = '?????????'
consumer_secret = '??????????'
access_token = '??????-???????'
access_token_secret = '???????'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
x = tweepy.API(auth, wait_on_rate_limit=True)

datos = {}
datos['tuits'] = []
contador_RTS = 0
contador_noRTS = 0
total = 0;

for tweets in tweepy.Cursor(x.search,
                       q='Piñera',
                       count=20,
                       result_type='recent').items(1000):
        if 'RT' in tweets.text:
                contador_RTS+=1
                print ('0')
                
                
        else:
                
                datos['tuits'].append({
                    'username': tweets.user.screen_name,
                    'contenido': tweets.text.rstrip('\n')})
                contador_noRTS+=1
                print (datos)
        print('Los tweets con RT son: ', contador_RTS)
        print('Los tweets sin RT son: ', contador_noRTS)
        print('Los tweets totales son: ', contador_RTS+contador_noRTS)
                


    
with open('data.json', 'w', encoding="utf-8") as file:
    json.dump(datos, file, indent=3, ensure_ascii=False)
    
