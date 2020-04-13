import bibtexparser

def main():
    with open('/home/rodolfosantana/Documentos/projetos/automator/BuscaImplacavel/bases/referencias/JABREF-2015-46.BibText') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    print(bib_database.entries[0]['title'])

    # x= biblib.BibTexFile('/Users/mac/Documents/projetos/automator/buscaimplacavel/bases/referencias/JABREF-2015-46.BibText')
    # bib = biblib.FileBibDB('/Users/mac/Documents/projetos/automator/buscaimplacavel/bases/referencias/JABREF-2015-46.BibText', mode='r')
    # print(bib)

if __name__ == '__main__':
    main()
