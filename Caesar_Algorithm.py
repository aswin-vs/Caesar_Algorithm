from tkinter import *

win = Tk()
win.title("Caesar Algorithm")
win.geometry("400x300+10+10")

def encrypt(t,s):
    
    cipher = ""

    # traverse text
    for i in range(len(t)):
        c = t[i]
 
        # Encrypt uppercase cacters
        if (c.isupper()):
            cipher += chr((ord(c) + s-65) % 26 + 65)
 
        # Encrypt lowercase cacters
        else:
            cipher += chr((ord(c) + s - 97) % 26 + 97)

    return str(cipher)

def call1():
    e3.delete(0, 'end')
    txt = e1.get()
    shift = int(e2.get())
    e3.insert(END,encrypt(txt,shift))

l1 = Label(win, text="Text")
l2 = Label(win, text="Shift")
l3 = Label(win, text="Cipher")

e1, e2, e3 = Entry(win), Entry(win), Entry(win)

b1 = Button(win, text="Encrypt", command=call1)

l1.place(x=100, y=50)
e1.place(x=200, y=50)
l2.place(x=100, y=100)
e2.place(x=200, y=100)
b1.place(x=200, y=150)
l3.place(x=100, y=200)
e3.place(x=200, y=200)

win.mainloop()