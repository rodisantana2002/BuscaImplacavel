# -*- coding: utf-8 -*-
# encoding: iso-8859-1

import re
import sys
import os
import logging

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine, LTAnon
from io import StringIO
from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)
arqOrigem = '../files/baixados/'
arqDestino = '../files/convertidos/'

class pdftotxt(object):

    def __init__(self):
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/pdftotxt.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

    def extrairConteudoPDF(self, arquivoPDF):
        logging.propagate = False
        logging.getLogger().setLevel(logging.ERROR)

        # PDFResourceManager Usado para armazenar recursos compartilhados
        # como fontes e imagens
        recursos = PDFResourceManager()
        buffer = StringIO()
        layoutParams = LAParams(line_margin=1, word_margin=0.3, char_margin=100)
        dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
        process_pdf(recursos, dispositivo, arquivoPDF, check_extractable=True)
        dispositivo.close()
        conteudo = buffer.getvalue()
        buffer.close()
        return conteudo

    def gerarTXT(self, arquivoRTF):

        rtf_file = "%s.rtf" % os.path.basename(arquivoRTF)[0:-4]
        txt_file = "%s.txt" % os.path.basename(arquivoRTF)[0:-4]

        try:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

            with open(arqDestino + txt_file, "w") as txt:
                fp = open(arqDestino + rtf_file, 'r')
                for linha in fp:
                    x = str(linha)

                    if x[0:1] == "\n":
                        y = x.replace('\n', "\n###")
                        txt.write(y)

                    elif x.startswith('\f'):
                        y = x.replace('\f', "\n@@@")
                        txt.write(y)

                    elif x.startswith(' \n'):
                        y = x.replace(' \n', "\n%%%")
                        txt.write(y)

                    elif x.startswith('\n '):
                        y = x.replace('\n ', "\n%%%")
                        txt.write(y)

                    elif x.endswith('\n'):
                        y = x.replace('\n', " ")
                        txt.write(y)

                    elif x.startswith(' '):
                        y = x.replace('\n', "\n%%%")
                        txt.write(y)

                    else:
                        txt.write(y)                        
            
            txt.close()
            fp.close()

            return '---> {} ---[ ok ] Arquivo convertido com sucesso [{}]'.format(data_atual, os.path.basename(arquivoRTF))

        except Exception:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser convertido'.format(data_atual)


    def gerarRTF(self, arquivoPDF):
        try:
            fp = open(arquivoPDF, 'rb')
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

            rtf_file = "%s.rtf" % os.path.basename(arquivoPDF)[0:-4]

            with open(arqDestino + rtf_file, "wb") as rtf:
                rtf.write(self.extrairConteudoPDF(fp).encode("utf-8"))
            rtf.close()    

            fp.close() 

            return '---> {} ---[ ok ] Arquivo convertido com sucesso [{}]'.format(data_atual, os.path.basename(arquivoPDF))

        except Exception:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser convertido'.format(data_atual)

    def converterPDF(self):
        logger.debug('----------------------------------------------------------------------------------------------')
        logger.debug('---> Iniciando conversão dos arquivos.')
        logger.debug('----------------------------------------------------------------------------------------------')

        opcao = input("----------:--> Informe o tipo desejadado (RTF - ajustes ou TXT - importação):")

        if opcao == 'TXT':
            tipo = ".rtf"
            arquivos = self.obterArquivos(arqDestino, tipo)
        else:    
            tipo = ".pdf"
            arquivos = self.obterArquivos(arqOrigem, tipo)        
        
        if len(arquivos) >= 2: 
            for arq in arquivos:
                if opcao =='TXT':
                    logger.debug(self.gerarTXT(arq))            
                else:
                    logger.debug(self.gerarRTF(arq))
        else:
            logger.debug('---> Não foram encontrados arquivos PDF para serem convertidos')

    def obterArquivos(self, path, tipo):    
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(tipo)])

def main():
    conv = pdftotxt()   
    conv.converterPDF()

if __name__ == '__main__':
    main()
