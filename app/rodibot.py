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

class base(object):
    """construtor"""
    def __init__(self, fileOUT):
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

        sci = SciHub()
        tmp_file = "%s.tmp" % self.fileOUT
        status = False

        with open(tmp_file, 'w') as tmp:
            writer = csv.DictWriter(tmp, fieldnames=self.FIELD_NAMES)
            writer.writeheader()

            with open(self.fileOUT, 'r') as source:
                reader = csv.DictReader(source)
                for row in reader:
                    if row['situacao'] == 'pendente':
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
                            logger.debug('%s', result['err'])
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
                            logger.debug('---[ ok ] Arquivo baixado com sucesso com identificador [%s]', row['id'])
        os.rename(tmp_file, self.fileOUT)
        return status

# carrega script
def main():
    bs = base('../bases/source.csv')
    bs.gerarFileBase()
    condicao = True
    tentativa=1
    while (condicao) :
        condicao = bs.processarDownload(tentativa)
        tentativa+=1


if __name__ == '__main__':
    main()
