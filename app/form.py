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
        self.showImg()
        
        # menu = Menu(self.master)
        # self.master.config(menu=menu)
        # file = Menu(menu)
        # file.add_command(label="Exit", command=self.client_exit)
        # menu.add_cascade(label="File", menu=file)
        # edit = Menu(menu)
        # edit.add_command(label="Show Img", command=self.showImg)
        # edit.add_command(label="Show Text", command=self.showText)
        # menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("../imagens/10.1109_ICSSSM.2012.6252346.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("1125x550")
app = Window(root)
root.mainloop()
