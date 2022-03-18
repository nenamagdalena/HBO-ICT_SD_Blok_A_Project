import psycopg2

def fetch_tweet_db():

    """"Functie print elke Tweet uit de database waar de status 'nieuw' is."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    # Als de status van de Tweet nieuw is wordt het geprint voor de moderator
    cur.execute("select inhoud from tweet where status='nieuw'")
    rows = cur.fetchall()

    list_tweets=[]
    for r in rows:
        list_tweets.append(f"{r[0]}")

    string_tweet = list_tweets[0]

    cur.close()
    con.close()

    return string_tweet

def fetch_mod_db():

    """"Functie geeft een lijst met namen van de moderatoren"""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    # Selecteert de naam en id van moderator
    cur.execute(f"select naam from moderator")
    rows = cur.fetchall()

    list_namen = []
    for r in rows:
        list_namen.append(f"{r[0]}")

    cur.close()
    con.close()

    return list_namen

def fetch_naam_db(tweet_inhoud):

    """"Functie geeft de naam en stationsnaam die bij de ingevoerde Tweet hoort."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    cur.execute("select naam, stationsnaam from tweet where inhoud = %s", [tweet_inhoud])

    rows = cur.fetchall()

    list_naam=[]
    list_stationsnaam=[]
    for r in rows:
        list_naam.append(f"{r[0]}")
        list_stationsnaam.append(f"{r[1]}")

    naam = list_naam[0]
    stationsnaam = list_stationsnaam[0]

    cur.close()
    con.close()

    return naam, stationsnaam

def fetch_afgekeurde_tweets_db():

    """"Functie print elke Tweet uit de database waar de status 'afgekeurd' is."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    # Als de status van de Tweet nieuw is wordt het geprint voor de moderator
    cur.execute("select naam, inhoud, datetime_tweet from tweet where status='afgekeurd'")
    rows = cur.fetchall()

    # Afgekeurde Tweets printen
    print("Afgekeurde Tweets:")
    print("Naam:          Tweet:                                                                          Datum/tijd:")
    for r in rows:
        print("{:15}{:80}{}".format(r[0], r[1], r[2]))



    cur.close()
    con.close()
