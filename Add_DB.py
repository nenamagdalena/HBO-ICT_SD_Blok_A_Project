import psycopg2
import datetime

def add_db(naam, stationsnaam, inhoud):

    """"Functie connect met de database en voegt de gegevens toe aan de database."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
        )

    cur = con.cursor()

    time = datetime.datetime.now()
    status = 'nieuw'

    # Als er geen naam is ingevuld in het entryveld, wordt er 'Anoniem' in de db ingevoerd
    if naam == '':
        db_naam = 'Anoniem'
    else:
        db_naam = naam

    # Voegt de gegevens toe aan de db
    cur.execute("insert into tweet (naam, stationsnaam, inhoud, datetime_tweet, status) values (%s, %s, %s, %s, %s)",
                    (db_naam, stationsnaam, inhoud, time, status))
    con.commit()
    cur.close()
    con.close()


def add_db_mod(id_mod, naam_mod):

    """Functie connect met de db en voegt de naam en id van de mod toe."""

    # Connect met de database
    con = psycopg2.connect(
        host='localhost',
        database='NS',
        user='postgres',
        password='CryingLightning97!'
    )

    cur = con.cursor()

    # Voegt het id en de naam van de mod toe aan de db
    cur.execute("insert into moderator (id_mod, naam) values (%s, %s)", (id_mod, naam_mod))

    con.commit()
    cur.close()
    con.close()