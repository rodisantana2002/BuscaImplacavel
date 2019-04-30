# -*- coding: utf-8 -*-
import re
import sys
import os
import logging
import argparse
import hashlib

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine, LTAnon
from io import StringIO

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)
arqOrigem = '../files/'
arqDestino = '../files/traduzidos/'


class convertepdf(object):

    def __init__(self):
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/converterpdf.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

    def extrairConteudoPDF(self, arquivoPDF):
        # PDFResourceManager Usado para armazenar recursos compartilhados
        # como fontes e imagens
        recursos = PDFResourceManager()
        buffer = StringIO()
        layoutParams = LAParams(line_margin=1, word_margin=0.3, char_margin=100, line_overlap=0.1, boxes_flow=0.1)
        dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
        process_pdf(recursos, dispositivo, arquivoPDF, check_extractable=False)
        dispositivo.close()
        conteudo = buffer.getvalue()
        buffer.close()
        return conteudo

    def gerarTXT(self, arquivoPDF):
        fp = open(arquivoPDF, 'rb')
        with open('convertedFile.txt', "wb") as txt_file:
            txt_file.write(self.extrairConteudoPDF(fp).encode("utf-8"))

        with open('lista.txt', "w") as txt:
            fp = open("convertedFile.txt", 'r')
            for linha in fp:    
                x = str(linha)
                if x.startswith("\n"):        
                    y = x.replace('\n', "\n ")
                    txt.write(y)
                elif x.startswith('\f'):
                    y = x.replace('\f', "\n @@")
                    txt.write(y)
                elif x.startswith(' \n'):
                    y = x.replace(' \n', "\n %%")
                    txt.write(y)
                elif x.endswith('\n'):   
                    y = x.replace('\n', " " )
                    txt.write(y)
        fp.close()            

    def converterPDF(self):
        for arq in self.obterArquivos(arqOrigem):
            print(arq)

    def obterArquivos(self, path):    
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(".pdf")])

def main():
    conv = convertepdf()
    # conv.gerarTXT("../files/arquivo.pdf")
    conv.converterPDF()

if __name__ == '__main__':
    main()
