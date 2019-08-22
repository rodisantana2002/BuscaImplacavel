
import re
import argparse
import hashlib
import logging
import os
import sys
import csv
import requests
import urllib3
import time
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from retrying import retry
import urllib.request

FIELD_NAMES_LISTA = ['id',
                     'nome',
                     'cidade',
                     'estado',
                     'tipo',
                     'local',
                     'resumo',
                     'url']


FIELD_NAMES_DETALHE = ['startup_id',
                       'mercado',
                       'publicoAlvo',
                       'modeloReceita',
                       'momento',
                       'site',
                       'fundacao',
                       'tamanhoTime',
                       'atualizacao',
                       'resumo']


def main():
    gerarListaStartups()
    # gerarDetalhesStartup()


def gerarListaStartups():
    arqIN = open('completo.txt', 'r')
    print('..lendo arquivo')
    soup = BeautifulSoup(arqIN, 'html5lib')
    id = 1
    print('..iniciando gravação')
    with open('startups_lista.csv', 'w') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=FIELD_NAMES_LISTA)
        writer.writeheader()

        tags = soup.findAll("div", {"class": "search-body__item"})
        for tag in tags:
            path = tag.find('a', href=True)
            url = "https://startupbase.com.br{}".format(path['href'])
            nome = tag.find("h3", {"class": "organization__title sb-size-6"})
            local = tag.find("p", {"class": "organization__label"})
            cidade = ""
            estado = ""
            tipo = ""

            local = local.getText().strip()
            col = 0
            try:
                if local.__len__() > 0:
                    col = local.index("-")
                    cidade = local[0:col].strip()
                    estado = local[col+1:col+4].strip()
                    tipo = local[col+5:].strip()
            except:
                pass

            resumo = tag.find(
                "p", {"class": "organization__description sb-size-10"})

            startup = {"id": id,
                       "cidade": cidade,
                       "estado": estado,
                       "tipo": tipo,
                       "nome": nome.getText().rstrip('\n'),
                       "local": local,
                       "resumo": resumo.getText().rstrip('\n'),
                       "url": url
                       }
            writer.writerow(startup)
            print(id, cidade, estado, tipo, local)
            print("--FIM-----------------")
            id = id+1


def gerarDetalhesStartup():

    with open('startups_lista.csv', 'r') as arq:
        reader = csv.DictReader(arq)

        with open('startups_destalhes.csv', 'a+') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=FIELD_NAMES_DETALHE)
            writer.writeheader()

            for row in reader:
                req = requests.get(row['url'])
                id = row['id']
                mercado = ""
                publicoAlvo = ""
                modeloReceita = ""
                momento = ""
                site = ""
                fundacao = ""
                tamanhoTime = ""
                atualizacao = ""
                resumo = ""

                if req.status_code == 200:
                    content = req.content
                    soup = BeautifulSoup(content, 'html.parser')

                    tagsHead = soup.findAll(
                        "p", {"class": "startup-timely__data has-text-weight-semibold sb-size-6"})
                    if tagsHead.__len__() > 0:
                        mercado = tagsHead[0].getText().strip()
                        publicoAlvo = tagsHead[1].getText().strip()
                        modeloReceita = tagsHead[2].getText().strip()
                        momento = tagsHead[3].getText().strip()
                        print("--INCIO-----------------")
                        print(mercado, publicoAlvo, modeloReceita, momento)

                    tagsBody = soup.findAll(
                        "p", {"class": "mold-text sb-size-10"})
                    if tagsBody.__len__() > 0:
                        site = tagsBody[0].getText().strip()
                        fundacao = tagsBody[1].getText().strip()
                        tamanhoTime = tagsBody[2].getText().strip()
                        atualizacao = tagsBody[3].getText().strip()
                        print(id, site, fundacao, tamanhoTime, atualizacao)

                    tagsResumo = soup.findAll(
                        "p", {"class": "mold-text mold-about__text sb-size-9"})
                    if tagsResumo.__len__() > 0:
                        resumo = tagsResumo[0].getText().strip()
                    print(resumo)
                    print("--FIM-----------------")

                    detail = {'startup_id': id,
                              'mercado': mercado,
                              'publicoAlvo': publicoAlvo,
                              'modeloReceita': modeloReceita,
                              'momento': momento,
                              'site': site,
                              'fundacao': fundacao,
                              'tamanhoTime': tamanhoTime,
                              'atualizacao': atualizacao,
                              'resumo': resumo}

                    writer.writerow(detail)


if __name__ == '__main__':
    main()
