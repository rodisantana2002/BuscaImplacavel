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

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
AVAILABLE_SCIHUB_BASE_URL = ['search.crossref.org']

class Processamento(object):

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = HEADERS
        self.available_base_url_list = AVAILABLE_SCIHUB_BASE_URL
        self.base_url = 'https://' + self.available_base_url_list[0] + '/'
        urllib3.disable_warnings()

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

    def importarReferencia(self, pathOrigem):
        # Passo 01 carregar dos dados para os arquivos bibtext
        arquivos = self._obterArquivos(pathOrigem, "bib")

        refs=[]        
        if len(arquivos) > 0:            
            for arq in arquivos:                                                
                with open(arq) as bibtex_file:
                    bib_database = bibtexparser.load(bibtex_file)
                    for ref in bib_database.entries:
                        # popula valores no objeto
                        referencia = Referencia()

                        if 'doi' in ref:
                            referencia.doi = ref['doi']
                        else:
                            referencia.doi = ""

                        if 'url' in ref:
                            referencia.url = ref['url']
                        else:
                            referencia.url = ""

                        if 'title' in ref:
                            referencia.titulo = ref['title']
                        else:
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
                            referencia.autores = ref['author']
                        else:
                            referencia.autores = ""

                        if 'abstract' in ref:
                            referencia.autores = ref['resumo']
                        else:
                            referencia.autores = ""

                        if 'keywords' in ref:
                            referencia.autores = ref['keywords']
                        else:
                            referencia.autores = ""

                        # adiciona na coleção
                        refs.append(referencia)                        
                        referencia.add(referencia)                       
        return refs