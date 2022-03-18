import psycopg2
import datetime


def update_db_goedgekeurd(id_mod, opmerking_moderator, inhoud_tweet):

    """"Functie connect met de database en update de gegevens in de database na goedkeuring van de Tweet."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    time_mod = datetime.datetime.now()
    status = 'goedgekeurd'

    # Update de status van de Tweet naar goedgekeurd en voegt de opmerking en datum en tijd toe aan de db
    sql = "update tweet set status = %s, opmerking_mod = %s, datetime_mod = %s, fkey_id_mod = %s where inhoud = %s"
    val = (status, opmerking_moderator, time_mod, id_mod, inhoud_tweet)
    cur.execute(sql,val)

    con.commit()
    cur.close()
    con.close()


def update_db_afgekeurd(id_mod, opmerking_moderator, inhoud_tweet):

    """"Functie connect met de database en update de gegevens in de database na afkeuring van de Tweet."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    time_mod = datetime.datetime.now()
    status= 'afgekeurd'

    # Update de status van de Tweet naar goedgekeurd en voegt de opmerking en datum en tijd toe aan de db
    sql = "update tweet set status = %s, opmerking_mod = %s, datetime_mod = %s, fkey_id_mod = %s where inhoud = %s"
    val = (status, opmerking_moderator, time_mod, id_mod, inhoud_tweet)
    cur.execute(sql,val)

    con.commit()
    cur.close()
    con.close()