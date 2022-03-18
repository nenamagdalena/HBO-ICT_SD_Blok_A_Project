from tkinter import *
from tkinter.messagebox import showinfo
from Fetch_DB import fetch_tweet_db, fetch_mod_db
from Add_DB import add_db_mod
from Update_DB import update_db_goedgekeurd, update_db_afgekeurd
from auth import consumer_key, consumer_secret, access_token_secret, access_token_key
from TwitterAPI import TwitterAPI
from PIL import Image, ImageTk

# TwitterAPI authorisation
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

# Tkinter hoofdschermroot maken
root = Tk()
root.geometry('500x420')                # Afmetingen achtergrond
root.configure(background='white')      # Achtergrondkleur

def clicked_goedkeuren():

    """"Functie geeft een pop-up weer voor de mod dat het bericht is goedgekeurd en update de row van de Tweet in de db.
    De goedgekeurde Tweet wordt ook gepost op Twitter."""

    try:
        # Foutmeldingen
        if len(entry_naam_moderator.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul naam in a.u.b.')
        elif len(entry_ID_mod.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul ID in a.u.b.')
        elif len(entry_opmerking.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul opmerking in a.u.b.')
        elif entry_naam_moderator.get() not in fetch_mod_db():
            bericht = 'Tweet is goedgekeurd.'
            showinfo(message=bericht)
            tweet_inhoud = fetch_tweet_db()
            # Updating de db
            add_db_mod(entry_ID_mod.get(), entry_naam_moderator.get())
            update_db_goedgekeurd(entry_ID_mod.get(), entry_opmerking.get(), tweet_inhoud)
            # De Tweet posten
            api.request('statuses/update', {'status': tweet_inhoud})
            # Volgende Tweet wordt uit de db gehaald
            tweet.configure(text=fetch_tweet_db())
        elif entry_naam_moderator.get() in fetch_mod_db():
            bericht = 'Tweet is goedgekeurd.'
            showinfo(message=bericht)
            tweet_inhoud = fetch_tweet_db()
            # Updating de db
            update_db_goedgekeurd(entry_ID_mod.get(), entry_opmerking.get(), tweet_inhoud)
            # De Tweet posten
            api.request('statuses/update', {'status': tweet_inhoud})
            # Volgende Tweet wordt uit de db gehaald
            tweet.configure(text=fetch_tweet_db())
    except:
        pass
        foutmelding.configure(text='Er zijn geen Tweets meer om te modereren.')

def clicked_afkeuren():

    """"Functie geeft een pop-up weer voor de mod dat het bericht is afgekeurd en update de row van de Tweet in de db.
    De Tweet wordt niet op Twitter geplaatst."""

    try:

        # Foutmeldingen
        if len(entry_naam_moderator.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul naam in a.u.b.')
        elif len(entry_ID_mod.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul ID in a.u.b.')
        elif len(entry_opmerking.get()) == 0:
            foutmelding.configure(text='Foutmelding: vul opmerking in a.u.b.')
        elif entry_naam_moderator.get() not in fetch_mod_db():
            bericht = 'Tweet is afgekeurd.'
            showinfo(message=bericht)
            tweet_inhoud = fetch_tweet_db()
            # Updating de db
            add_db_mod(entry_ID_mod.get(), entry_naam_moderator.get())
            update_db_afgekeurd(entry_ID_mod.get(), entry_opmerking.get(), tweet_inhoud)
            # Volgende Tweet wordt uit de db gehaald
            tweet.configure(text=fetch_tweet_db())
        elif entry_naam_moderator.get() in fetch_mod_db():
            bericht = 'Tweet is afgekeurd.'
            showinfo(message=bericht)
            tweet_inhoud = fetch_tweet_db()
            # Updating de db
            update_db_afgekeurd(entry_ID_mod.get(), entry_opmerking.get(), tweet_inhoud)
            # Volgende Tweet wordt uit de db gehaald
            tweet.configure(text=fetch_tweet_db())
    except:
        pass
        foutmelding.configure(text='Er zijn geen Tweets meer om te modereren.')

# Label voor titel
titel = Label(master=root,
              text='Modereren NS Tweets',
              background='#f7d117',
              foreground='#00387b',
              font=('Tahoma', 14, 'bold'),
              width=30,
              height=2)
titel.pack(fill=X)

# NS Logo
ns_logo = ImageTk.PhotoImage(Image.open(r"C:\Users\2008n\PycharmProjects\Programming\PROJA\nslogo.jpg"))
ns_logo_lbl = Label(image=ns_logo, borderwidth=0)
ns_logo_lbl.place(x=10, y=12)

# Label en entryveld voor naam moderator
naam_mod = Label(master=root,
                text='Naam moderator',
                background='white',
                foreground='#00387b',
                font=('Tahoma', 10, 'bold'),
                width=13,
                height=2)
naam_mod.place(x=30,y=60)

entry_naam_moderator = Entry(master=root, background ='#F0F0F0', width=25)
entry_naam_moderator.place(x=30, y=90)

# Label en entryveld voor ID moderator
ID_mod = Label(master=root,
             text='ID moderator',
             background='white',
             foreground='#00387b',
             font=('Tahoma', 10, 'bold'),
             width=10,
             height=2)
ID_mod.place(x=250,y=60)

entry_ID_mod = Entry(master=root, background ='#F0F0F0', width=25)
entry_ID_mod.place(x=250,y=90)

# Label voor weergeven Tweet
display_tweet = Label(master=root,
             text='Tweet:',
             background='white',
             foreground='#00387b',
             font=('Tahoma', 10, 'bold'),
             width=6,
             height=2)
display_tweet.place(x=30,y=115)


# Weergeeft de Tweet
tweet = Label(master=root,
             text=fetch_tweet_db(),              # Fetch de eerstvolgende Tweet uit de db
             background='#f7d117',
             foreground='#00387b',
             font=('Tahoma', 10, 'bold'),
             width=50,
             height=2,
              wraplength=350)
tweet.place(x=30,y=150, width=440, height=70)

# Label en entryveld voor opmerking moderator
opmerking = Label(master=root,
              text='Opmerking:',
              background='white',
              foreground='dark blue',
              font=('Tahoma', 10, 'bold'),
              width=9,
              height=2)
opmerking.place(x=30,y=230)

entry_opmerking = Entry(master=root, background ='#F0F0F0', width=140)
entry_opmerking.place(x=30,y=270, width=440, height=60)

# Label voor foutmelding
foutmelding = Label(master=root,
              text='',
              background='white',
              foreground='red',
              font=('Tahoma', 10),
              width=60,
              height=2)
foutmelding.place(x=30,y=335)

# Goedkeuren button toevoegen
button1 = Button(master=root,
                text='Goedkeuren',
                bg='#f7d117',
                fg='#00387b',
                font=('Tahoma', 9, 'bold'),
                command=clicked_goedkeuren)
button1.place(x=120, y=380)

# Afkeuren button toevoegen
button2 = Button(master=root,
                text='Afkeuren',
                bg='#f7d117',
                fg='#00387b',
                font=('Tahoma', 9, 'bold'),
                command=clicked_afkeuren)
button2.place(x=270, y=380)

mainloop()