# -*- coding: utf-8 -*-
# encoding: iso-8859-1


"""
@author Rodolfo Santana
"""
from __future__ import unicode_literals, absolute_import
import re
import argparse
import hashlib
import logging
import os
import sys
import requests
import certifi
import urllib3
import time

from PIL import Image, ImageTk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from retrying import retry
import urllib.request

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

# constants
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
AVAILABLE_SCIHUB_BASE_URL = ['www.crossref.org']


class doi(object):
    
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = HEADERS
        self.available_base_url_list = AVAILABLE_SCIHUB_BASE_URL
        self.base_url = 'https://' + self.available_base_url_list[0] + '/'
        urllib3.disable_warnings()

    @retry(wait_random_min=2000, wait_random_max=10000, stop_max_attempt_number=2)
    def obter(self, identifier):
        """
        Carrega a página 'Crossref' e passa identificação do artigo a ser pesquisa 
        """
        data = self.fetch(self.base_url)

        if not 'err' in data:
            # self._save(data['pdf'], os.path.join(destination, path if path else data['name']))
            print('oi')
        return data        

    def fetch(self, url):
        """
        Busca o artigo recuperando primeiro o link direto para o pdf.
        Se o identificador for um pay-wall DOI, PMID ou URL, use o Sci-Hub
        para acessar e baixar o paper. Caso contrário, basta baixar o paper diretamente.
        """

        try:
            res = self.sess.get(url, verify=False)
            driver = webdriver.Chrome(ChromeDriverManager("2.41").install())
            driver.get(url)
            elem = driver.find_element_by_xpath('//*[@id="tabs-search"]/li[2]/a')
            elem.click()

            elem = driver.find_element_by_id('metadatasearchbox')
            strCaptcha = "Tang, K., Jiang, Z.B., Sun, W., Zhang, X., Dong, W.S., 2010. Research on tenant placement based on business relations. In: IEEE 7th Inter- national Conference on e-Business Engineering (ICEBE), 2010. IEEE, pp. 479–483."
            elem.send_keys(strCaptcha)
            elem.submit()

            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/a')
            elem.click()

            elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/span/ul/li[3]/a')
            elem.click()

            res = self.sess.get(driver.current_url, verify=False)
            soup = BeautifulSoup(res.content, 'html.parser')
            print(soup)
            # str_path = soup.findAll("pre", {"id": "citation-text"})
            # for attr in elem.get_property('attributes'):
            #     attrs.append([attr['name'], attr['value']])


            # soup = BeautifulSoup(res.content, 'html.parser')
            # str_doi = soup.findAll("div", {"id": "item-links"})
            # i=0
            # lin=0
            # for linha in str_doi[0]:                
            #     if i==1:
            #         for x in linha:                    
            #             if lin==2:
            #                 print(x)
            #             lin=lin+1    
            #     i=i+1    

            driver.close()
            return "x"


        #             # tratamento cado carrege a pagina com o pdf e sem o captcha
        #             elem = driver.find_element_by_name("answer")
        #             if elem.is_displayed():
        #                 strCaptcha = input("informe o captcha: ")
        #                 elem.send_keys(strCaptcha)
        #                 elem.submit()
        #                 res = self.sess.get(driver.current_url, verify=False)
        #                 driver.close()

        #             if res.headers['Content-Type'] != 'application/pdf':
        #                 return {'err': '---[erro] Falha: %s (url) captcha informado esta incorreto' % (identifier)}

        #             else:
        #                 return {
        #                     'pdf': res.content,
        #                     'url': url,
        #                     'name': self._generate_name(res)
        #                 }

        #         elif self.viewPDF == "hide":
        #             # View com abertura do Browser
        #             driver = webdriver.PhantomJS()
        #             driver.get(url)

        #             driver.set_window_size(1300, 550)
        #             images = driver.find_elements_by_tag_name('img')

        #             if len(images) > 0:
        #                 for image in images:
        #                     src = image.get_attribute('src')
        #                     name = identifier.split('/')[-1]
        #                     urllib.request.urlretrieve(
        #                         src, "../imagens/" + name.lower() + ".png")
        #                     im = Image.open(
        #                         "../imagens/" + name.lower() + ".png")
        #                     im.show()

        #                     elem = driver.find_element_by_name("answer")
        #                     strCaptcha = input("informe o captcha: ")
        #                     elem.send_keys(strCaptcha)
        #                     elem.submit()
        #                     res = self.sess.get(
        #                         driver.current_url, verify=False)

        #                 if res.headers['Content-Type'] != 'application/pdf':
        #                     return {'err': '---[erro] Falha: %s (url) captcha informado esta incorreto' % (identifier)}

        #                 else:
        #                     return {
        #                         'pdf': res.content,
        #                         'url': url,
        #                         'name': self._generate_name(res)
        #                     }

        #             else:
        #                 return {'err': '---[erro] Falha: %s (url) não foi localizada a imagem do captcha, verifique manualmente o DOI' % (identifier)}

        #     else:
        #         return {
        #             'pdf': res.content,
        #             'url': url,
        #             'name': self._generate_name(res)
        #         }

        except requests.exceptions.ConnectionError:
            logger.debug(
                '---> Impossível acessar a url {}'.format(self.available_base_url_list[0]))
            return {'err': '---[erro] Falha: %s (url) não foi possível estabeler a conexão com os servidores' % (identifier)}

        except requests.exceptions.RequestException as exc:
            return {'err': exc}


def main():
    sh = doi()
    sh.obter("")

if __name__ == '__main__':
    main()
