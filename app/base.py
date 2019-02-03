# -*- coding: utf-8 -*-
# encoding: iso-8859-1
import sys
import csv

FIELD_NAMES = ['id',
               'title',
               'year',
               'author',
               'doi',
               'url',
               'keywords',
               'tipo',
               'base',
               'situacao',
               'numTentativas',
               'possuiCaptcha',
               'valorCaptcha',
               'msgRetorno']

class base(object):
    """docstring for ."""
    def __init__(self, fileIN, fileOUT):
        self.fileIN = fileIN
        self.fileOUT = fileOUT

    def gerarFileBase(self):
        with open(self.fileOUT, 'w') as source:
            writer = csv.DictWriter(source, fieldnames=FIELD_NAMES)
            writer.writeheader()
            with open(self.fileIN, 'r') as base:
                reader = csv.DictReader(base)
                print ('+--------------------------------------------------+')
                print ('|     Inciando script de captura de arquivos       |')
                print ('+--------------------------------------------------+')
                for row in reader:
                    writer.writerow({'id':row['Identifier'],
                                     'title':row['Title'],
                                     'year':row['Year'],
                                     'author':row['Author'],
                                     'doi':row['DOI'],
                                     'url':row['URL'],
                                     'keywords':row['Custom3'],
                                     'tipo':row['Publisher'],
                                     'base':row['BibliographyType'],
                                     'situacao':'none',
                                     'numTentativas':0,
                                     'possuiCaptcha':'none',
                                     'valorCaptcha':'none',
                                     'msgRetorno':''
                                    })
                    # print leitura
                    print ('--->', row['Identifier'],'[',row['DOI'],']')
        print ('+--------------------------------------------------+')
        print (' ---> finalizando preparação do arquivo base...')

# carrega script
def main():
    bs = base('../strings/Base.csv', '../strings/source.csv')
    bs.gerarFileBase()

if __name__ == '__main__':
    main()
