# -*- coding: utf-8 -*-
# encoding: iso-8859-1

import re
import sys
import os
import logging
import csv
import time

from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

pathOrigem = '../files/convertidos/'
pathDestino = '../files/traduzidos/'

class translate(object):

    def __init__(self):
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/translate.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

        self.FIELD_NAMES = ['id',
                            'arquivo',
                            'tipo',
                            'txtorigem',
                            'txttranslate',
                            'datahoracarga', 
                            'datahoratranslate']

    def popularDados(self, arquivoTXT):
        try:
            csv_file = "%s.csv" % os.path.basename(arquivoTXT)[0:-4]

            with open(pathDestino + csv_file, 'w') as tmp:
                writer = csv.DictWriter(tmp, fieldnames=self.FIELD_NAMES)
                writer.writeheader()
                id = 1
                with open(arquivoTXT, 'r') as source:
                    for row in source:
                        data_hora_atuais = datetime.now()
                        data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

                        if row[0:3] == '###' or row[0:3] == 'TIT' or row[0:3] == 'ABS' or row[0:3] == 'WOR' or row[0:3] == 'REF':
                            id += 1
                            writer.writerow({'id':id,
                                            'arquivo':os.path.basename(arquivoTXT)[0:-4],
                                            'tipo': row[0:3],
                                            'txtorigem':row[3:],
                                            'txttranslate':'',
                                            'datahoracarga':data_atual,
                                            'datahoratranslate': ''
                                            })

            return '---> {} ---[ ok ] Foram carregadas [{}] linhas com sucesso'.format(data_atual, id)

        except Exception:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser carregado'.format(data_atual)

    def traduzirDados(self, arquivoCSV):
        try:
            csv_file = "%s.csv" % os.path.basename(arquivoCSV)[0:-4]

            with open(pathDestino + csv_file, 'w') as tmp:
                writer = csv.DictWriter(tmp, fieldnames=self.FIELD_NAMES)
                writer.writeheader()
                id = 1
                with open(arquivoCSV, 'r') as source:
                    for row in source:
                        data_hora_atuais = datetime.now()
                        data_atual = data_hora_atuais.strftime(
                            '%d/%m/%Y %H:%M:%S')

                        if not row.isblank():
                            id += 1
                            writer.writerow({'id': id,
                                             'arquivo': os.path.basename(arquivoCSV)[0:-4],
                                             'tipo': row[0:3],
                                             'txtorigem': row[3:],
                                             'txttranslate': '',
                                             'datahoracarga': data_atual,
                                             'datahoratranslate': ''
                                             })

            return '---> {} ---[ ok ] Foram carregadas [{}] linhas com sucesso'.format(data_atual, id)

        except Exception:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser carregado'.format(data_atual)


    def carregarRepositoriosCSV(self):
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Iniciando processo de carga nos repositórios CSV.')
        logger.debug('----------------------------------------------------------')

        # Passo 01 carregar dos dados para os arquivos csv 
        arquivos = self.obterArquivos(pathOrigem)

        if len(arquivos) > 0:
            for arq in arquivos:
                logger.debug(self.popularDados(arq))

            logger.debug('----------------------------------------------------------')
            
        else:
            logger.debug('---> Não foram encontrados arquivos TXT para serem lidos')

    def traduzirDados(self):
        logger.debug('----------------------------------------------------------')
        logger.debug('---> Iniciando processo de tradução dos arquivos.')
        logger.debug('----------------------------------------------------------')

        # Passo 01 ler arquivos csv e processar tradução e atualização dos dados
        arquivos = self.obterArquivos(pathDestino)

        if len(arquivos) > 0:
            for arq in arquivos:
                logger.debug(self.traduzirDados(arq))

            logger.debug(
                '----------------------------------------------------------')

        else:
            logger.debug(
                '---> Não foram encontrados arquivos CSV para serem traduzidos')

    def obterArquivos(self, path):
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(".txt")])

def main():
    trans = translate()
    trans.carregarRepositoriosCSV()
    # trans.traduzirDados()

if __name__ == '__main__':
    main()


'''
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
'''
