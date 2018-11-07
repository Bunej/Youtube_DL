from tkinter import *
from tkinter import messagebox
import youtube_dl
import sys

root = Tk()
root.resizable(0, 0)


def save():
    ydl_opts = {
        'outtmpl': 'downloaded music/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([e1.get()])
    messagebox.showinfo('Success', 'Download completed')


def exit():
    sys.exit()


root.title('Youtube downloader')
l1 = Label(root, text='Download MP3 from Youtube', font=20)
l1.pack()
e1 = Entry(root, width=50)
e1.pack()
b1 = Button(root, text='Download', width=7, height=2, command=save)
b1.pack(side=LEFT)
b2 = Button(root, text='Exit', command=exit, width=7, height=2)
b2.pack(side=RIGHT)

root.mainloop()
