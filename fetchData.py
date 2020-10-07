from tkinter import *
import pyrebase
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

config = {
    "apiKey": "AIzaSyDErG5f2Ith5wgF7iIDTLFJFJZdTAuseZ8",
    "authDomain": "tic-tac-toe-16.firebaseapp.com",
    "databaseURL": "https://tic-tac-toe-16.firebaseio.com/",
    "storageBucket": "tic-tac-toe-16.appspot.com",
    # "serviceAccount": "C:\\Users\\Arth\\Desktop\\Tic Tac Toe\\tic-tac-toe-16-firebase-adminsdk-8r063-7fa1664978.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    users = db.child("online").get().val()
    online_users = users['users']
    online_users_label.config(text="Online Users : "+str(online_users))

def online_user_stream_handler(message):
    user_names = db.child("online").get().val()
    online_users_names = user_names['name']
    online_users_names = online_users_names.replace(',','\n')
    t.delete('1.0', END)
    t.insert(END, str(online_users_names))
    t.pack(side=TOP, fill=X)

online_stream = db.child("online").stream(stream_handler)

def main_tic_tac_toe():
    global main_
    main_ = Tk()
    main_.geometry("300x250")
    main_.title("Tic Tac Toe")
    global online_users_label
    online_users_label = Label(width="250", height="3", font=("Calibri", 13))
    online_users_label.config(text="Loading..")
    online_users_label.pack()
    Button(text="Online Users", height="2", width="30", command=online_users).pack()
    Button(text="Play with Random", height="2", width="30", command=random).pack()
    Button(text="Play with Friend", height="2", width="30", command=lambda: friend_input.pack()).pack()
    # Button(text='Click to hide Label',command=lambda: friend_input.pack_forget()).pack()
    # Button(text='Click to show Label', command=lambda: friend_input.pack()).pack()
    Label(text="").pack()
    friend_input = Entry(width=20)
    main_.mainloop()

def online_users():
    global online_users_screen
    online_users_screen = Toplevel(main_)
    online_users_screen.title("Online Users")
    online_users_screen.geometry("300x270")
    global online_user_names_label
    global t
    h = Scrollbar(online_users_screen, orient='horizontal')
    h.pack(side=BOTTOM, fill=X)
    v = Scrollbar(online_users_screen)
    v.pack(side=RIGHT, fill=Y)
    t = Text(online_users_screen, width=40, height=15, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    online_user_stream = db.child("online").stream(online_user_stream_handler)
    online_users_screen.mainloop()

def random():
    showinfo("Tic Tac Toe", "Play Random")

def friend():
    showinfo("Tic Tac Toe", "Play with friend")

def on_closing_main():
    online_stream.close()
    sys.exit()

main_tic_tac_toe()
