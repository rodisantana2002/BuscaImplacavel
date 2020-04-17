import bibtexparser
from sqlalchemy import create_engine
import PySimpleGUI as sg


class tela(object):

    def __init__(self):
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Button('enviar')],
            [sg.Ok('')]
        ]
        janela = sg.Window("Dados").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

def main():

    layout  = [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('To Do List Example', layout)

    event, values = window.read()
    # with open('/home/rodolfosantana/Documentos/projetos/automator/buscaimplacavel/bases/referencias/JABREF-2015-46.BibText') as bibtex_file:
    #     bib_database = bibtexparser.load(bibtex_file)
    # print(bib_database.entries[0]['title'])

    # engine = create_engine('sqlite:///../buscaimplacavel/bases/database/bot.db')

    # x= biblib.BibTexFile('/Users/mac/Documents/projetos/automator/buscaimplacavel/bases/referencias/JABREF-2015-46.BibText')
    # bib = biblib.FileBibDB('/Users/mac/Documents/projetos/automator/buscaimplacavel/bases/referencias/JABREF-2015-46.BibText', mode='r')
    # print(bib)

if __name__ == '__main__':
    main()
