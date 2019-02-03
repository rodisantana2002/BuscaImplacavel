# -*- coding: utf-8 -*-
# encoding: iso-8859-1
import sys
import csv
import logging
from scihub import *


# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

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
        self.sci = SciHub()

    def gerarFileBase(self):
        with open(self.fileOUT, 'w') as source:
            writer = csv.DictWriter(source, fieldnames=FIELD_NAMES)
            writer.writeheader()
            with open(self.fileIN, 'r') as base:
                reader = csv.DictReader(base)
                logger.debug('+--------------------------------------------------+')
                logger.debug('|     Inciando script de captura de arquivos       |')
                logger.debug('+--------------------------------------------------+')
                count = 1
                for row in reader:
                    if count <= 10:
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

                        strLog = '---> {0} - {1}'.format(row['Identifier'], row['DOI'])
                        logger.debug(strLog)
                    count+=1

        logger.debug ('----------------------------------------------------------')
        logger.debug ('---> Finalizando preparação do arquivo base.')

    def processarDownload(self):

        logger.debug ('----------------------------------------------------------')
        logger.debug ('---> Inicializando tentativas de downloads dos aqruivos.')

        with open(self.fileOUT, 'r') as source:
            reader = csv.DictReader(source)
            for row in reader:
                # strLog = '---> Tentativa para [{0} - {1}]'.format(row['id'], row['doi'])
                # logger.debug(strLog)
                result = self.sci.download(row['doi'], path=row['id'])

                if 'err' in result:
                    logger.debug('%s', result['err'])
                else:
                    logger.debug('Arquivo baixado com sucesso com identificador [%s]', row['id'])

# carrega script
def main():
    bs = base('../strings/Base.csv', '../strings/source.csv')
    bs.gerarFileBase()
    bs.processarDownload()

if __name__ == '__main__':
    main()
