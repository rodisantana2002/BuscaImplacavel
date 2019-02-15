from __future__ import unicode_literals, absolute_import
from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("Identificador de Captcha")
        self.pack(fill=BOTH, expand=2)
        self.showTitulo("Identificador: ")
        self.showImg("../imagens/10.1109_ROMAN.2014.6926404.png")

    def showImg(self, path):
        load = Image.open(path)
        render = ImageTk.PhotoImage(load, master=self.master)
        self.img = Label(self, image=render)
        self.img.image = render
        self.img.place(x=0, y=0)
        self.img.pack()

    def showTitulo(self, title):
        lblTitulo = Label(self, text=title, font=("Helvetica", 16), height=(1))        
        lblTitulo.pack()

# root = Tk()
# root.geometry("1125x700")
# app = Window(root)
# root.mainloop()
