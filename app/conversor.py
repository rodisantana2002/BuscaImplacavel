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

class conversor(object):
    # construtor
    def __init__(self, origem, destino, limite):
        self.homeDir = "../logs"
        self.logFile= self.homeDir + '/conversor.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)

        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

        self.limite = limite
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
        for arquivo in self.files_path(self.origem):
            with open(self.destino, 'w+') as source:
                writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
                writer.writeheader()
                with open(arquivo, 'r') as base:
                    reader = csv.DictReader(base)
                    logger.debug('+--------------------------------------------------+')
                    logger.debug('|     Inciando script de conversão de arquivos     |')
                    logger.debug('+--------------------------------------------------+')
                    count = 1
                    for row in reader:
                        if count <= self.limite:
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

        logger.debug ('----------------------------------------------------------')
        logger.debug ('---> Finalizando preparação do arquivo base.')

    def files_path(self, path):
        '''return list of string'''
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(".csv")])

# carrega script
def main():
    # carrega parametros de chamada
    parser = argparse.ArgumentParser(description='RodoBot - Removendo as barreiras da ciência.')
    parser.add_argument('-p',  '--lista', metavar='path', help='irá converter todos arquivos .csv encontrados no path:', default='', type=str)
    parser.add_argument('-l',  '--limit', metavar='N', help='o limite de conversao é limitado em:', default=0, type=int)
    args = parser.parse_args()

    bs = conversor(args.lista, '../bases/source.csv', limite=args.limit)
    bs.gerarFileBase()


if __name__ == '__main__':
    main()
