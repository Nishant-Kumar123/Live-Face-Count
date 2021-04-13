from tkinter import *
import tkinter as tk

def info():
    info = Tk()
    info.geometry("300x100")
    info.title("HelpDesk")

    tk.Label(info, text="Contact us  :  18002000047", font="30").pack()
    tk.Label(info, text="for complaints  :  middaymeal@gmail.com", font="30").pack()

    ab = tk.Button(info, text="Exit", command=info.destroy, fg="white", bg="blue", font="10")
    ab.place(x=130, y=60, width=50)