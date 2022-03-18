from tkinter import *
from tkinter.messagebox import showinfo
from Add_DB import add_db
from PIL import Image, ImageTk

root = Tk()                             # Creëer het hoofdschermroot.
root.geometry('500x400')                # Afmetingen achtergrond
root.configure(background='white')      # Achtergrondkleur

def clicked():

    """"Functie geeft bij een aantal constraints een foutmelding. Als aan alle condities zijn voldaan volgt een pop-up
    met bericht voor de gebruiker en voegt de entries toe aan de db"""

    if len(entry_station.get()) == 0:
        foutmelding.configure(text='Foutmelding: Geef a.u.b. een stationsnaam op.')
    elif len(entry_tweet.get()) == 0:
        foutmelding.configure(text='Foutmelding: Vul a.u.b. een Tweet in.')
    elif len(entry_tweet.get()) > 140:
        foutmelding.configure(text='Foutmelding: Tweet is langer dan 140 tekens. Pas aan a.u.b.')
    else:
        foutmelding.configure(text='')
        bericht = 'Tweet is verstuurd, bedankt!'
        showinfo(message=bericht)
        add_db(entry_naam.get(), entry_station.get(), entry_tweet.get())


# Label voor titel
titel = Label(master=root,
              text='NS Twitterzuil',
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

# Label voor onderschrift 1
onderschrift = Label(master=root,
              text='Welkom bij de NS Twitterzuil! Laat uw feedback over de NS achter.',
              background='white',
              foreground='#00387b',
              font=('Tahoma', 11),
              width=30,
              height=2)
onderschrift.pack(fill=X)

# Label voor onderschrift 2
onderschrift2 = Label(master=root,
              text='(Tweets kunnen op Twitter geplaatst worden. U kunt anoniem blijven door geen naam in te vullen.)',
              background='white',
              foreground='#00387b',
              font=('Tahoma', 8),
              width=30,
              height=1)
onderschrift2.pack(fill=X)

# Label en entryveld voor stationsnaam
station = Label(master=root,
                text='Stationsnaam',
                background='white',
                foreground='#00387b',
                font=('Tahoma', 10, 'bold'),
                width=11,
                height=2)
station.place(x=30,y=120)

entry_station = Entry(master=root, background ='#F0F0F0', width=25)
entry_station.place(x=30, y=160)

# Label en entryveld voor naam
naam = Label(master=root,
             text='Naam',
             background='white',
             foreground='#00387b',
             font=('Tahoma', 10, 'bold'),
             width=5,
             height=2)
naam.place(x=250,y=120)

entry_naam = Entry(master=root, background ='#F0F0F0', width=25)
entry_naam.place(x=250,y=160)

# Label en entryveld voor tweet
tweet = Label(master=root,
              text='Tweet (max. 140 tekens)',
              background='white',
              foreground='#00387b',
              font=('Tahoma', 10, 'bold'),
              width=22,
              height=2)
tweet.place(x=20,y=200)

entry_tweet = Entry(master=root, background ='#F0F0F0', width=140)
entry_tweet.place(x=30,y=240, width=440, height=60)

# Label voor foutmelding
foutmelding = Label(master=root,
              text='',
              background='white',
              foreground='red',
              font=('Tahoma', 10,),
              width=60,
              height=2)
foutmelding.place(x=30,y=305)

# Tweet button toevoegen
button = Button(master=root,
                text='Tweet',
                bg='#f7d117',
                fg='#00387b',
                font=('Tahoma',11, 'bold'),
                command=clicked)
button.place(x=215, y=350)

mainloop()                # Toon het hoofdscherm