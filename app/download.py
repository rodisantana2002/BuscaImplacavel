from __future__ import unicode_literals, absolute_import

from builtins import input
import bibtexparser
# from . import __version__
# from lxml.etree import ParserError
import re
from title2bib.crossref import get_bib_from_title
from capcha import SciHub

# headers = {"Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}

libgen_xpath_pdf_url = "/html/body/table/tr/td[3]/a"
xpath_captcha = "//*[@id='captcha']"
xpath_pdf = "//*[@id='pdf']"
xpath_input = "/html/body/div/table/tbody/tr/td/form/input"
xpath_form = "/html/body/div/table/tbody/tr/td/form"
domain_scihub = "http://sci-hub.tw/"


ScrapSci = SciHub(headers,xpath_captcha, xpath_pdf, xpath_input, xpath_form, domain_scihub)

def start_scihub():
    ScrapSci.start()

def download_from_scihub(doi, png_file):
    found, r = ScrapSci.navigate_to(doi, png_file)
    has_captcha, has_iframe = ScrapSci.check_captcha()

def download_from_doi(doi, location="../imagens/", use_libgen=False):
    pdf_name = "{}".format(doi.replace("/", "_"))
    png_file = location + pdf_name
    download_from_scihub(doi, png_file)
