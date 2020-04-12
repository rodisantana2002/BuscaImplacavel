# -*- coding: utf-8 -*-
# encoding: iso-8859-1


"""
@author Rodolfo Santana
"""
import re
import logging
import os
import sys
import requests
import urllib3
import time
import urllib.request

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from retrying import retry
from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
AVAILABLE_SCIHUB_BASE_URL = ['search.crossref.org']

pathOrigem = '../bases/referencias/'
pathDestino = '../bases/origem/'

class referencia(object):
    
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = HEADERS
        self.available_base_url_list = AVAILABLE_SCIHUB_BASE_URL
        self.base_url = 'https://' + self.available_base_url_list[0] + '/'
        urllib3.disable_warnings()
        
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/referencia.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

        self.FIELD_NAMES = ['id',
                            'arquivo_origem',
                            'arquivo_destino',
                            'doi',
                            'ano',
                            'source']               


    def gerarReferencias(self):
        """
        Carrega a página 'Crossref' e passa identificação do artigo a ser pesquisa 
        """
        self.carregarRepositoriosTXT() 
        return ""        


    def popularDados(self, arquivoTXT):
        try:
            refs = []
            fp = open(arquivoTXT, 'r')
            for linha in fp:                
                refs.append(linha)
            fp.close() 
                       
            return refs

        except Exception as exc:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser carregado'.format(data_atual)

    def carregarRepositoriosTXT(self):
        logger.debug('----------------------------------------------------------------------------------------------')
        logger.debug('---> Iniciando processo de carga nos repositórios TXT.')
        logger.debug('----------------------------------------------------------------------------------------------')

        # Passo 01 carregar dos dados para os arquivos txt
        arquivos = self.obterArquivos(pathOrigem, "txt")
        files=[]
        
        if len(arquivos) > 0:
            for arq in arquivos:
                files.append(arq)
                logger.debug('----------------------------------------------------------------------------------------------')
            
        else:
            logger.debug('---> Não foram encontrados arquivos TXT para serem lidos')
        
        return files    


    def obterArquivos(self, path, tipo):
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith("." + tipo)])

    
    @retry(wait_random_min=2000, wait_random_max=10000, stop_max_attempt_number=2)
    def obterReferencia(self, referencia):
        """
        Busca o artigo recuperando primeiro o link direto para o pdf.
        """
        try:
            # carrega a página de pesquisa da CROSSREF
            # res = self.sess.get(self.base_url, verify=False)
            driver = webdriver.Chrome(ChromeDriverManager("2.41").install())
            # driver = webdriver.PhantomJS()
            driver.get(self.base_url)
            
            # localiza input de pesquisa e injeta referencia a ser pesquisada
            elem = driver.find_element_by_id('search-input')
            elem.send_keys(referencia)
            elem.submit()  
            time.sleep(5)                     
            
            # localiza primeira ref. e aciona a opção "actions"
            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/a')
            elem.click()
            time.sleep(5)

            # localiza e aciona a opção BIBTEXT
            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/ul/li[1]/a')
            elem.click()
            time.sleep(5)
            
            # aciona a opção no modal para garantir que seja carregado
            elem = driver.find_element_by_xpath('//*[@id="bibtex"]/a') 
            elem.click()           
            time.sleep(15)
            
            # localiza e extrai o valor do BIBTEXT
            elem = driver.find_element_by_xpath('//*[@id="citation-text"]')            
            var = elem.text
            
            return var                    
            driver.quit()            

        except requests.exceptions.ConnectionError:
            return 'err'
        except requests.exceptions.RequestException as exc:
            return 'err'

def main():
    sh = referencia()
    refs=[]
    bibs=[]
    
    # carregas os arquivos
    for file in sh.carregarRepositoriosTXT():
        for ref in sh.popularDados(file):
            refs.append(ref)
            
    for ref in refs:
        bibs.append(sh.obterReferencia(ref))

    
    # var = [] 
    # var.append('Ali, M. et al.: Security in cloud computing: Opportunities and challenges. Information Sciences. 305, 357–383 (2015).')
    # var.append('Alshamaila, Y. et al.: Cloud computing adoption by SMEs in the north east of England: A multi-perspective framework. Journal of Enterprise Information Management. 26, 3, (2013).')
    
    
    
    # for i in var:
    #     bibs.append(sh.obterReferencia(i))
        
    print(refs)

if __name__ == '__main__':
    main()
