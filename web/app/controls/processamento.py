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
import bibtexparser

from app.model.models import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from retrying import retry
from datetime import datetime

from googletrans import Translator

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
AVAILABLE_SCIHUB_BASE_URL = ['search.crossref.org']


# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

class Processamento(object):

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = HEADERS
        self.available_base_url_list = AVAILABLE_SCIHUB_BASE_URL
        self.base_url = 'https://' + self.available_base_url_list[0] + '/'
        urllib3.disable_warnings()

        # logs
        self.homeDir = "../web/app/logs"
        self.logFile = self.homeDir + '/translate_referencia.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)


    @retry(wait_random_min=2000, wait_random_max=10000, stop_max_attempt_number=2)
    def obterReferencia(self, referencia):
        try:

            # carrega a página de pesquisa da CROSSREF
            # res = self.sess.get(self.base_url, verify=False)
            # driver = webdriver.Chrome(ChromeDriverManager("2.41").install())
            driver = webdriver.PhantomJS()
            driver.get(self.base_url)

            # localiza input de pesquisa e injeta referencia a ser pesquisada
            elem = driver.find_element_by_id('search-input')
            elem.send_keys(referencia)
            elem.submit()
            time.sleep(5)

            # localiza primeira ref. e aciona a opção "actions"
            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/a')
            elem.click()
            time.sleep(10)

            # localiza e aciona a opção BIBTEXT
            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/ul/li[1]/a')
            elem.click()
            time.sleep(15)

            # # aciona a opção no modal para garantir que seja carregado
            # elem = driver.find_element_by_xpath('//*[@id="bibtex"]/a')
            # elem.click()
            # time.sleep(10)

            # localiza e extrai o valor do BIBTEXT
            elem = driver.find_element_by_xpath('//*[@id="citation-text"]')
            var = elem.text

            return var
            driver.quit()

        except requests.exceptions.ConnectionError:
            return 'err'
        except requests.exceptions.RequestException as exc:
            return 'err'

    def importarReferencia(self, strBibText):
        refs=[]                
        if len(strBibText.strip()) > 0:            
            bib_database = bibtexparser.loads(strBibText)
            
            logger.debug('----------------------------------------------------------------------------------------------')
            logger.debug('---> Iniciando processo de Tradução das Referências.')            

            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')            

            try:
                for ref in bib_database.entries:
                    # popula valores no objeto                    
                    referencia = Referencia()
                    referencia.situacao = "Pendente"
                    
                    if 'doi' in ref:
                        referencia.doi = ref['doi']
                    else:
                        referencia.doi = ""

                    if 'url' in ref:
                        referencia.url = ref['url']
                    else:
                        referencia.url = ""

                    if 'title' in ref:
                        referencia.title = ref['title'].replace("{", "").replace("}", "")
                        referencia.titulo = self._processarTraducao(ref['title'].replace("{", "").replace("}", ""))
                    else:
                        referencia.title = ""
                        referencia.titulo = ""

                    if 'year' in ref:
                        referencia.ano = ref['year']
                    else:
                        referencia.ano = ""

                    if 'publisher' in ref:
                        referencia.publisher = ref['publisher']
                    else:
                        referencia.publisher = ""
        
                    if 'booktitle' in ref:
                        referencia.bookTitulo = ref['booktitle']
                    else:
                        referencia.bookTitulo = ""

                    if 'author' in ref:
                        referencia.autores = ref['author'].replace("{", "").replace("}", "")
                    else:
                        referencia.autores = ""

                    if 'abstract' in ref:
                        referencia.abstract = ref['abstract'].replace("{", "").replace("}", "")
                        referencia.resumo = self._processarTraducao(ref['abstract'].replace("{", "").replace("}", ""))
                    else:
                        referencia.abstract = ""
                        referencia.resumo = ""

                    if 'keywords' in ref:
                        referencia.keywords = ref['keywords']
                    else:
                        referencia.keywords = ""

                    # adiciona na coleção
                    refs.append(referencia)                        
                    logger.debug('---> {} ---[  ok  ] referência traduzida com sucesso! [{}]'.format(data_atual, referencia.doi))

            except:
                logger.debug('---> {} ---[ erro ] referência não foi traduzida [{}]'.format(data_atual, referencia.doi))

        logger.debug('----------------------------------------------------------------------------------------------')
        logger.debug('---> Finalizando processo de Tradução das Referências.')            

        return refs

    def _processarTraducao(self, strOrigem):
        strDestino = ""
        try:
            trans = Translator()
            txtTranslate = trans.translate(strOrigem, dest='pt')
            strDestino = txtTranslate.text
        except Exception:
            strDestino = "Erro na tradução"

        return strDestino