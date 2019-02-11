# -*- coding: utf-8 -*-
# encoding: iso-8859-1

import sys
import csv
import os
import logging
import scihub as sc
from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

class base(object):
    """construtor"""
    def __init__(self, fileOUT):
        self.homeDir = "../logs"
        self.logFile= self.homeDir + '/rodibot.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

        self.fileOUT = fileOUT
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

    def processarDownload(self, numTentativa):
        logger.debug ('----------------------------------------------------------')
        logger.debug ('---> Inicializando tentativa [%s] de downloads dos aqruivos.' % numTentativa)

        sci = sc.SciHub()
        tmp_file = "%s.tmp" % self.fileOUT
        status = False

        with open(tmp_file, 'w') as tmp:
            writer = csv.DictWriter(tmp, fieldnames=self.FIELD_NAMES)
            writer.writeheader()

            with open(self.fileOUT, 'r') as source:
                reader = csv.DictReader(source)
                for row in reader:
                    if row['situacao'] == 'pendente':
                        data_hora_atuais = datetime.now()
                        data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
                        result = sci.download(row['doi'], destination='../files', path=row['id'])

                        if 'err' in result:
                            writer.writerow({'id':row['id'],
                                             'title':row['title'],
                                             'year':row['year'],
                                             'author':row['author'],
                                             'doi':row['doi'],
                                             'url':row['url'],
                                             'keywords':row['keywords'],
                                             'tipo':row['tipo'],
                                             'base':row['base'],
                                             'numTentativas':numTentativa,
                                             'situacao':'pendente',
                                             'possuiCaptcha':'yes',
                                             'valorCaptcha':'none',
                                             'msgRetorno': result['err']
                                            })
                            logger.debug('%s %s', data_atual, result['err'])
                            status=True
                        else:
                            writer.writerow({'id':row['id'],
                                             'title':row['title'],
                                             'year':row['year'],
                                             'author':row['author'],
                                             'doi':row['doi'],
                                             'url':row['url'],
                                             'keywords':row['keywords'],
                                             'tipo':row['tipo'],
                                             'base':row['base'],
                                             'numTentativas':numTentativa,
                                             'situacao':'finalizado',
                                             'possuiCaptcha':'none',
                                             'valorCaptcha':'none',
                                             'msgRetorno': 'Arquivo baixado com sucesso'
                                            })
                            logger.debug('%s ---[ ok ] Arquivo baixado com sucesso com identificador [%s]', data_atual, row['id'])
        os.rename(tmp_file, self.fileOUT)
        return status

    def _isBlank (self, myString):
        if myString and myString.strip():
            return False
        return True

# carrega script e roda em modo força-bruta
def main():
    bs = base('../bases/source.csv')
    condicao = True
    tentativa=1
    while (condicao) :
        condicao = bs.processarDownload(tentativa)
        tentativa+=1


if __name__ == '__main__':
    main()
