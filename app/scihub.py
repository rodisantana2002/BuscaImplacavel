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
import requests
import urllib3
import bibtexparser

from bs4 import BeautifulSoup
from retrying import retry
from capcha import Capcha

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

# constants
SCIHUB_BASE_URL = 'http://sci-hub.tw/'
SCHOLARS_BASE_URL = 'https://scholar.google.com/scholar'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
AVAILABLE_SCIHUB_BASE_URL = ['sci-hub.se','sci-hub.tw']

libgen_xpath_pdf_url = "/html/body/table/tr/td[3]/a"
xpath_captcha = "//*[@id='captcha']"
xpath_pdf = "//*[@id='pdf']"
xpath_input = "/html/body/div/table/tbody/tr/td/form/input"
xpath_form = "/html/body/div/table/tbody/tr/td/form"
domain_scihub = "http://sci-hub.tw/"

class SciHub(object):
    """
    SciHub class permite a pesquisa de papers no Google Scholars
    e lista e baixa os arquivos do sci-hub.io
    """

    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = HEADERS
        self.available_base_url_list = AVAILABLE_SCIHUB_BASE_URL
        self.base_url = 'http://' + self.available_base_url_list[0] + '/'
        self.capcha = Capcha(HEADERS, xpath_captcha, xpath_pdf, xpath_input, xpath_form, domain_scihub)
        self.capcha.start()

    def download_from_scihub(self, doi, png_file):
        found, r = self.capcha.navigate_to(doi, png_file)
        has_captcha, has_iframe = self.capcha.check_captcha()


    def download_from_doi(self, doi, location="../imagens/", use_libgen=False):
        pdf_name = "{}".format(doi.replace("/", "_"))
        png_file = location + pdf_name
        self.download_from_scihub(doi, png_file)

    def set_proxy(self, proxy):
        '''
        set proxy for session
        :param proxy_dict:
        :return:
        '''
        if proxy:
            self.sess.proxies = {
                "http": proxy,
                "https": proxy, }

    def _change_base_url(self):
        # del self.available_base_url_list[0]
        self.base_url = 'http://' + self.available_base_url_list[0] + '/'
        logger.debug("---> Alterando source {}".format(self.available_base_url_list[0]))

    @retry(wait_random_min=100, wait_random_max=10000, stop_max_attempt_number=10)
    def download(self, identifier, destination='', path=None):
        """
        Faz o download de um documento do sci-hub com um identificador (DOI, PMID, URL).
        Atualmente, isso pode potencialmente ser bloqueado por um captcha se um certo
        limite foi alcançado.
        """
        data = self.fetch(identifier)

        if not 'err' in data:
            self._save(data['pdf'], os.path.join(destination, path if path else data['name']))
        return data

    def fetch(self, identifier):
        """
        Busca o artigo recuperando primeiro o link direto para o pdf.
        Se o identificador for um pay-wall DOI, PMID ou URL, use o Sci-Hub
        para acessar e baixar o papel. Caso contrário, basta baixar o papel diretamente.
        """
        try:
            url = self._get_direct_url(identifier)
            res = self.sess.get(url, verify=False)

            if res.headers['Content-Type'] != 'application/pdf':
                self.download_from_doi(identifier)
                return {'err': '---[erro] Falha: %s (url) identificou uso de captcha' % (identifier)}
            else:
                return {
                    'pdf': res.content,
                    'url': url,
                    'name': self._generate_name(res)
                }

        except requests.exceptions.ConnectionError:
            logger.debug('Impossível acessar {}, alterando url'.format(self.available_base_url_list[0]))
            self._change_base_url()

        except requests.exceptions.RequestException as e:
            return {'err': e}

    def _get_direct_url(self, identifier):
        """
        Localiza o URL de origem direto para um determinado identificador.
        """
        id_type = self._classify(identifier)

        return identifier if id_type == 'url-direct' \
            else self._search_direct_url(identifier)

    def _search_direct_url(self, identifier):
        """
        O Sci-Hub incorpora documentos em um iframe.
        Esta função encontra a URL da fonte real que parece algo como https://sci-hub.io/.../....pdf.
        """
        res = self.sess.get(self.base_url + identifier, verify=False)
        s = self._get_soup(res.content)
        iframe = s.find('iframe')
        if iframe:
            return iframe.get('src') if not iframe.get('src').startswith('//') \
                else 'http:' + iframe.get('src')

    def _classify(self, identifier):
        """
        Classifica o tipo de identificador:
        url-direct - arquivo sempre acessível
        url-non-direct - arquivo pagos e fechados
        pmid - PubMed ID
        doi - digital object identifier
        """
        if (identifier.startswith('http') or identifier.startswith('https')):
            if identifier.endswith('pdf'):
                return 'url-direct'
            else:
                return 'url-non-direct'
        elif identifier.isdigit():
            return 'pmid'
        else:
            return 'doi'

    def _save(self, data, path):
        """
        Salvar um arquivo fornece dados e um caminho.
        """
        with open(path, 'wb') as f:
            f.write(data)

    def _get_soup(self, html):
        """
        Return html soup.
        """
        return BeautifulSoup(html, 'html.parser')

    def _generate_name(self, res):
        """
        Gerar nome de arquivo exclusivo para arquivo. Retorna um nome calculando
        md5 hash do conteúdo do arquivo e, em seguida, os últimos 20 caracteres foram adicionados
        da URL que normalmente fornece um bom identificador de papel.
        """
        name = res.url.split('/')[-1]
        name = re.sub('#view=(.+)', '', name)
        pdf_hash = hashlib.md5(res.content).hexdigest()
        return '%s-%s' % (pdf_hash, name[-20:])

def main():
    sh = SciHub()

    parser = argparse.ArgumentParser(description='SciHub - To remove all barriers in the way of science.')
    parser.add_argument('-d',  '--download', metavar='(DOI|PMID|URL)', help='tenta encontrar e baixar o arquivo', type=str)
    parser.add_argument('-f',  '--file', metavar='path', help='utilizado para realizar o Download por meio arquivo com lista de URLs', type=str)
    parser.add_argument('-l',  '--limit', metavar='N', help='o limite de pesquisa é limitado em:', default=10, type=int)
    parser.add_argument('-o',  '--output', metavar='path', help='diretorio para armazenar os documentos', default='', type=str)
    args = parser.parse_args()

    if args.download:
        result = sh.download(args.download, args.output)
        if 'err' in result:
            logger.debug('%s', result['err'])
        else:
            logger.debug('---[ ok ] Arquivo baixado com sucesso com identificador [%s]', args.download)
    elif args.file:
        with open(args.file, 'r') as f:
            identifiers = f.read().splitlines()
            for identifier in identifiers:
                result = sh.download(identifier, args.output)
                if 'err' in result:
                    logger.debug('%s', result['err'])
                else:
                    logger.debug('---[ ok ] Arquivo baixado com sucesso com identificador [%s]', identifier)


if __name__ == '__main__':
    main()
