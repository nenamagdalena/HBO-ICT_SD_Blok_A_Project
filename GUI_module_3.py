from tkinter import *
from auth import consumer_key, consumer_secret, access_token_secret, access_token_key
from TwitterAPI import TwitterAPI, TwitterPager
from Fetch_DB import fetch_naam_db
import requests
import json
from PIL import Image, ImageTk

# Tweets verkrijgen van het Twitteraccount
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

username = 'test_NS_Tweets'
pager = TwitterPager(api,
                     'statuses/user_timeline',
                     {'screen_name': username, 'count': 200})

# Alle Tweets in een lijst zetten
recent_tweets = []
for item in pager.get_iterator(wait=3.5):
    recent_tweets.append(item['text'])


# Weer API
api_key = "1d82076731db9f0195f6a151b0e7d493"
# Coordinaten voor Utrecht
lat = 52.5
lon = 5.7
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}&units=metric"

# Fetching de naam en stationsnaam uit de db om weer te geven


def refresh_tweet():

    """"Functie haalt de laatste Tweet van de lijst weg en configured de tekst van de Tweet naar de volgende samen met
    de naam van degene die het getweet heeft."""

    try:
        recent_tweets.pop()
        naam, stationsnaam = fetch_naam_db(recent_tweets[-1])
        display_tweet.configure(text=recent_tweets[-1])
        display_naam.configure(text=f'{naam} Tweette op station {stationsnaam}:')
        root.after(5000, refresh_tweet)
    except:
        # Als de lijst met Tweets leeg is wordt het weerbericht van nu in Utrecht weergeven
        response = requests.get(url)
        data = json.loads(response.text)
        display_naam.configure(text='Het weer in Utrecht:', font=('Tahoma', 12, 'bold'))
        display_tweet.configure(text=f"Temperatuur: {data['current']['temp']} °C \n"
                                     f"Voelt als: {data['current']['feels_like']} °C", font=('Tahoma', 11, 'bold'))

# GUI
root = Tk()                         # Creëer het hoofdschermroot.
root.geometry('500x275')            # Afmetingen achtergrond
root.configure(background='white')  # Achtergrondkleur

# Label voor titel
titel = Label(master=root,
              text='NS op Twitter',
              background='#f7d417',
              foreground='#00387b',
              font=('Tahoma', 14, 'bold'),
              width=30,
              height=2)
titel.pack(fill=X)

# NS Logo
ns_logo = ImageTk.PhotoImage(Image.open(r"C:\Users\2008n\PycharmProjects\Programming\PROJA\nslogo.jpg"))
ns_logo_lbl = Label(image=ns_logo, borderwidth=0)
ns_logo_lbl.place(x=10, y=12)

# Border Tweet
border = Label(master=root,
               text='',
               background='#f7d117',
               foreground='#00387b',
               font=('Tahoma', 10, 'bold'),
               width=100,
               height=2)
border.place(x=30, y=70, width=440, height=170)

naam, stationsnaam = fetch_naam_db(recent_tweets[-1])

# Naam display
display_naam = Label(master=root,
                      text=f"{naam} Tweette op station {stationsnaam}:",
                      background='#f7d117',
                      foreground='#00387b',
                      font=('Tahoma', 10, 'bold'),
                      width=35,
                      height=2)
display_naam.place(x=35, y=70)

# Tweet display
display_tweet = Label(master=root,
                      text=recent_tweets[-1],
                      background='white',
                      foreground='#00387b',
                      font=('Tahoma', 11),
                      width=100,
                      height=10,
                      wraplength=350)
display_tweet.place(x=50, y=110, width=400, height=110)

# Na 5 seconden wordt de volgende Tweet weergegeven
root.after(5000, refresh_tweet)

mainloop()