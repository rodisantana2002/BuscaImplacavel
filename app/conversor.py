# -*- coding: utf-8 -*-
# encoding: iso-8859-1
import re
import argparse
import hashlib
import sys
import csv
import os
import logging

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)
arqBase='../bases/source.csv'

class conversor(object):
    # construtor
    def __init__(self, origem, destino, limiteInf, limiteSup):
        self.homeDir = "../logs"
        self.logFile= self.homeDir + '/conversor.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

        self.limiteInf = limiteInf
        self.limiteSup = limiteSup
        self.origem = origem #sempre recebe uma lista
        self.destino = destino
        self.FIELD_NAMES = ['id',
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

    def gerarFileBase(self):
        strNone='------------------------------------------------------------'
        with open(self.destino, 'w+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            writer.writeheader()

        for arquivo in self.files_path(self.origem):
            if arquivo.lower().__contains__('jabref'):
                self._carregarJabref(arquivo)

            elif arquivo.lower().__contains__('ieee'):
                self._carregarIEEE(arquivo)

            elif arquivo.lower().__contains__('springer'):
                self._carregarSpringer(arquivo)

            elif arquivo.lower().__contains__('acm'):
                self._carregarACM(arquivo)

            elif arquivo.lower().__contains__('sciencedirect'):
                self._carregarScience(arquivo)

            else:
                strNone='------------------------------------------------------------'


        logger.debug (strNone)
        logger.debug ('---> Finalizando preparação do arquivo base.')

    def files_path(self, path):
        '''return list of string'''
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(".csv")])

    def _carregarJabref(self, arquivo):
        with open(self.destino, 'a+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            with open(arquivo, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+----------------------------------------------------------+')
                logger.debug('|     Inciando script de conversão de arquivos (JabRef)    |')
                logger.debug('+----------------------------------------------------------+')
                count = 1
                for row in reader:
                    if count >= self.limiteInf and count <= self.limiteSup:
                        writer.writerow({'id':row['Identifier'],
                                         'title':row['Title'],
                                         'year':row['Year'],
                                         'author':row['Author'],
                                         'doi':row['DOI'],
                                         'url':row['URL'],
                                         'keywords':row['Custom3'],
                                         'tipo':row['Publisher'],
                                         'base':row['BibliographyType'],
                                         'situacao':'pendente',
                                         'numTentativas':'none',
                                         'possuiCaptcha':'none',
                                         'valorCaptcha':'none',
                                         'msgRetorno':''
                                        })

                        strLog = '---> {0} - {1}'.format(row['Identifier'], row['DOI'])
                        logger.debug(strLog)
                    count+=1

    def _carregarIEEE(self, arquivo):
        with open(self.destino, 'a+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            with open(arquivo, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+----------------------------------------------------------+')
                logger.debug('|      Inciando script de conversão de arquivos (IEEE)     |')
                logger.debug('+----------------------------------------------------------+')
                count = 1
                for row in reader:
                    if count <= self.limiteInf:
                        writer.writerow({'id': 'IEEE-{0}-{1}'.format(row['Publication_Year'], count),
                                         'title':row['Document Title'],
                                         'year':row['Publication_Year'],
                                         'author':row['Authors'],
                                         'doi':row['DOI'],
                                         'url':row['PDF Link'],
                                         'keywords':'none',
                                         'tipo':row['Publisher'],
                                         'base':row['Document Identifier'],
                                         'situacao':'pendente',
                                         'numTentativas':'none',
                                         'possuiCaptcha':'none',
                                         'valorCaptcha':'none',
                                         'msgRetorno':''
                                        })

                        strLog = '---> {0} - {1}'.format(row['Publication_Year'], row['DOI'])
                        logger.debug(strLog)
                    count+=1

    def _carregarSpringer(self, arquivo):
        with open(self.destino, 'a+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            with open(arquivo, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+----------------------------------------------------------+')
                logger.debug('|    Inciando script de conversão de arquivos (Springer)   |')
                logger.debug('+----------------------------------------------------------+')
                count = 1
                for row in reader:
                    if count <= self.limiteInf:
                        writer.writerow({'id':'Springer-{0}-{1}'.format(row['Publication Year'], count),
                                         'title':row['Item Title'],
                                         'year':row['Publication Year'],
                                         'author':row['Authors'],
                                         'doi':row['Item DOI'],
                                         'url':row['URL'],
                                         'keywords':'none',
                                         'tipo':'Springer',
                                         'base':row['Content Type'],
                                         'situacao':'pendente',
                                         'numTentativas':'none',
                                         'possuiCaptcha':'none',
                                         'valorCaptcha':'none',
                                         'msgRetorno':''
                                        })

                        strLog = '---> {0} - {1}'.format(row['Publication Year'], row['Item DOI'])
                        logger.debug(strLog)
                    count+=1

    def _carregarACM(self, arquivo):
        with open(self.destino, 'a+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            with open(arquivo, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+----------------------------------------------------------+')
                logger.debug('|     Inciando script de conversão de arquivos (ACM)       |')
                logger.debug('+----------------------------------------------------------+')
                count = 1
                for row in reader:
                    if count <= self.limiteInf:
                        writer.writerow({'id':'ACM-{0}-{1}'.format(row['id'], row['year']),
                                         'title':row['title'],
                                         'year':row['year'],
                                         'author':row['author'],
                                         'doi':row['doi'],
                                         'url':'none',
                                         'keywords':'none',
                                         'tipo':row['publisher'],
                                         'base':row['type'],
                                         'situacao':'pendente',
                                         'numTentativas':'none',
                                         'possuiCaptcha':'none',
                                         'valorCaptcha':'none',
                                         'msgRetorno':''
                                        })

                        strLog = '---> {0} - {1}'.format(row['id'], row['doi'])
                        logger.debug(strLog)
                    count+=1

    def _carregarScience(self, arquivo):
        with open(self.destino, 'a+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            writer.writeheader()
            with open(arquivo, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+----------------------------------------------------------+')
                logger.debug('|    Inciando script de conversão de arquivos (Science)    |')
                logger.debug('+----------------------------------------------------------+')
                count = 1
                for row in reader:
                    if count <= self.limiteInf:
                        writer.writerow({'id':row['Identifier'],
                                         'title':row['Title'],
                                         'year':row['Year'],
                                         'author':row['Author'],
                                         'doi':row['DOI'],
                                         'url':row['URL'],
                                         'keywords':'none',
                                         'tipo':row['Publisher'],
                                         'base':row['BibliographyType'],
                                         'situacao':'pendente',
                                         'numTentativas':'none',
                                         'possuiCaptcha':'none',
                                         'valorCaptcha':'none',
                                         'msgRetorno':''
                                        })

                        strLog = '---> {0} - {1}'.format(row['Identifier'], row['DOI'])
                        logger.debug(strLog)
                    count+=1

# carrega script
def main():
    # carrega parametros de chamada
    parser = argparse.ArgumentParser(description='RodoBot - Removendo as barreiras da ciência.')
    parser.add_argument('-p',  '--lista', metavar='path', help='irá converter todos arquivos .csv encontrados no path:', default='', type=str)
    parser.add_argument('-l',  '--limit_inf', metavar='N', help='o limite de conversao é limitado em:', default=0, type=int)
    parser.add_argument('-s',  '--limit_sup', metavar='N', help='o limite de conversao é limitado em:', default=0, type=int)
    args = parser.parse_args()

    bs = conversor(args.lista, arqBase, limiteInf=args.limit_inf, limiteSup=args.limit_sup)
    bs.gerarFileBase()


if __name__ == '__main__':
    main()
