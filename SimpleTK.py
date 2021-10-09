from tkinter import *
import tkinter.messagebox

window = Tk()
# add widgets here

def createWindow(windowTitle, Geometry):
    window.title(windowTitle)
    window.geometry(Geometry)
    window.mainloop()

def createButton(X, Y, Text, Color, BackgroundColor, Center, Command):
    if (Center == False):
        btn=Button(window, text=Text, fg=Color, bg=BackgroundColor, command=Command)
        btn.place(x=X, y=Y)
    else:
        btn=Button(window, text=Text, fg=Color, bg=BackgroundColor, command=Command)
        btn.config(anchor='center')
        btn.pack()

def createText(X, Y, Text, Color, BackgroundColor, Font, Center):
    if (Center == False):
        lbl=Label(window, text=Text, fg=Color, bg=BackgroundColor, font=Font)
        lbl.place(x=X, y=Y)
    else:
        lbl=Label(window, text=Text, fg=Color, bg=BackgroundColor, font=Font)
        lbl.config(anchor='center')
        lbl.pack()

def setIconICO(File):
    window.iconbitmap(File)

def setIconPNG(File):
    window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file=File))

def createMessageBoxInfo(Title, Text):
    tkinter.messagebox.showinfo(Title, Text)

def createMessageBoxError(Title, Text):
    tkinter.messagebox.showerror(Title, Text)

def createMessageBoxWarning(Title, Text):
    tkinter.messagebox.showwarning(Title, Text)

def setBackground(Color):
    window.configure(background=Color)