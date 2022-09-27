from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x600")
root.title("yt video downloader")

def download():
    
    try:
        
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("video download successfully")
        
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter correct link")
        
Label(root, text="Welcome to youtube \n Downloader Application", font="consolas 15 bold").pack()
myVar = StringVar()
myVar.set("enter your link")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)

root.mainloop()
        
        


