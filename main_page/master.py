import tkinter as tk
from tkinter import *
from module.info import info as info
from module.myclick import myclick as myclick


def project():
    if (e1.get() == "meal" and e2.get() == "1234"):

        root.destroy()

        master = Tk()
        master.geometry("500x500")
        master.title("Welcome")

        mybutton1 = Button(master, text="Check Live", command=myclick, fg="white", bg="red", font="50")
        mybutton1.place(x=180, y=150, width=200)

        mybutton3 = Button(master, text="HelpDesk", command=info, fg="white", bg="red", font="50")
        mybutton3.place(x=180, y=200, width=200)

        mybutton4 = Button(master, text="Exit", command=master.destroy, fg="white", bg="red", font="50")
        mybutton4.place(x=180, y=250, width=200)

        master.mainloop()
    else:

        mylabel1 = tk.Label(root, text="Invalid Username or Password", fg="red")
        mylabel1.place(x=500, y=220)


root = Tk()
root.geometry("1000x500")
root.title("System Login")
    # Definging the first row
lblfrstrow = tk.Label(root, text ="Username  -",font="50")
lblfrstrow.place(x = 350, y = 150)

e1 = tk.Entry(root, width = 35)
e1.place(x = 500, y = 150, width = 200)

lblsecrow = tk.Label(root, text ="Password  -",font="50")
lblsecrow.place(x = 350, y = 200)

e2 = tk.Entry(root, width = 35,show="*")
e2.place(x = 500, y = 200, width = 200)

mybutton=Button(root, text="Submit",command=project, fg="white", bg="blue",font="50")
mybutton.place(x = 425, y = 300, width = 100)
    #e1.get()
root.mainloop()



