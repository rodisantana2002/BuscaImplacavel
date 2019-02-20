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

    def processarDownload(self, numTentativa, modo):
        logger.debug ('----------------------------------------------------------')
        logger.debug ('---> Inicializando tentativa [%s] de downloads dos arquivos.' % numTentativa)

        if modo == "view":           
            sci = sc.SciHub(viewPDF=modo)
        elif modo == "hide":   
            sci = sc.SciHub(viewPDF=modo)
        else:
            sci = sc.SciHub(viewPDF=modo)

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
                        result = sci.download(row['doi'], destination='../files', path=row['id'] + ".pdf")

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
                            logger.debug('---> %s %s', data_atual, result['err'])
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
                            logger.debug('---> %s --[ ok ] Arquivo baixado com sucesso com identificador [%s]', data_atual, row['id'] + ".pdf")
        os.rename(tmp_file, self.fileOUT)
        return status

# carrega script e roda em modo força-bruta
def main():
    bs = base('../bases/source.csv')
    condicao = True    
    tentativa=1

    logger.debug('----------------------------------------------------------')
    logger.debug('-- Seja bem vindo ao RodiBot, o que deseja que eu faça? --')
    logger.debug('----------------------------------------------------------')
    logger.debug('--> [1] Download de aquivos (exibe browser para leitura do captcha)')
    logger.debug('--> [2] Download de aquivos (exibe apenas imagem para leitura do captcha)')
    logger.debug('--> [3] Download de aquivos (não solicita o input do catcha, quando detectado)')
    logger.debug('--> [0] Finalizar o Bot')
    logger.debug('----------------------------------------------------------')
    opcao = input("informe a opção desejada:")

    if str(opcao) == "1":
        while (condicao):
            condicao=bs.processarDownload(tentativa, "view")
            tentativa += 1
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Encerrando processo de download de arquivo.')

    elif str(opcao) == "2": 
        while (condicao):
            condicao = bs.processarDownload(tentativa, "hide")
            tentativa += 1
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Encerrando processo de download de arquivo.')
    
    elif str(opcao) == "3":
        while (condicao):
            condicao = bs.processarDownload(tentativa, "none")
            tentativa += 1
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Encerrando processo de download de arquivo.')

    elif str(opcao) == "0":
        logger.debug('---> Encerrando processo de download de arquivo.')

    else:
        logger.debug('---> Opção informada (%s) não existe no menu' % opcao)
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Encerrando processo de download de arquivo.')

if __name__ == '__main__':
    main()
