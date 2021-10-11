from tkinter import *
import tkinter.messagebox

window = Tk()

def createWindow(windowTitle=None, Geometry=None):
    window.title(windowTitle)
    window.geometry(Geometry)
    window.mainloop()

def createButton(X=None, Y=None, Text=None, Color=None, BackgroundColor=None, Center=None, Command=None):
    if (Center):
        btn=Button(window, text=Text, fg=Color, bg=BackgroundColor, command=Command)
        btn.config(anchor='center')
        btn.pack()
    else:
        btn=Button(window, text=Text, fg=Color, bg=BackgroundColor, command=Command)
        btn.place(x=X, y=Y)

def createText(X=None, Y=None, Text=None, Color=None, BackgroundColor=None, Font=None, Center=None):
    if (Center):
        lbl=Label(window, text=Text, fg=Color, bg=BackgroundColor, font=Font)
        lbl.config(anchor='center')
        lbl.pack()
    else:
        lbl=Label(window, text=Text, fg=Color, bg=BackgroundColor, font=Font)
        lbl.place(x=X, y=Y)

def setIconICO(File):
    window.iconbitmap(File)

def setIconPNG(File):
    window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file=File))

def createMessageBoxInfo(Title=None, Text=None):
    tkinter.messagebox.showinfo(Title, Text)

def createMessageBoxError(Title=None, Text=None):
    tkinter.messagebox.showerror(Title, Text)

def createMessageBoxWarning(Title=None, Text=None):
    tkinter.messagebox.showwarning(Title, Text)

def setBackground(Color):
    window.configure(background=Color)

def updateScreen():
    window.update()

def updateIdleTasks():
    window.update_idletasks() 

def setTitle(Title):
    window.title(Title)

def destroy():
    window.destroy()

def setResizable(Resizable):
    if (Resizable):
        None
    else:
        window.resizable(FALSE, FALSE)