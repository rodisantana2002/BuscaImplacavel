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
        self.showImg("../imagens/10.1109_ICSSSM.2012.6252346.png")
        self.showText("iden")

    def showImg(self, path):
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self, title):
        text = Label(self, text=title, font=("Helvetica", 16), height=(2))
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("1125x550")
app = Window(root)
root.mainloop()
