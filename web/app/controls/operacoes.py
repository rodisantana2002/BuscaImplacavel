import os
import string
import csv

from flask import Flask, Blueprint
from app.model.models import *
from app.controls.utils import *
from app.controls.referencia import *
from sqlalchemy import DateTime, func, desc

operacoes = Blueprint("operacoes", __name__)

class Operacoes():

    def __init__(self):
        self.authentic = {"code": "", "msg": "", "id": "", "value": "", "superuser": ""}
        self.pesquisa = Pesquisa()
        self.processo = Processo()
        self.processoFile = ProcessoFile()
        self.processoFileReferencia = ProcessoFileReferencia()
        self.referencia = Referencia()

    def obterPesquisas(self):
        return self.pesquisa.query.all()

    def obterProcessos(self):
        return self.processo.query.order_by(Processo.id.desc()).all()

    def obterProcessoById(self, id):
        return self.processo.query.filter_by(id=id).first()

    def registrarProcesso(self, Processo):
        try:
            obj = Processo
            obj.add(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro efetuado com sucesso!"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"
        return self.authentic

    def registrarProcessoArquivo(self, ProcessoFile):
        try:
            file = self.processoFile.query.filter_by(name_file=ProcessoFile.name_file, processo_id=ProcessoFile.processo_id).first()
            if file != None:
               self.authentic["code"] = "500"
               self.authentic["msg"] = "Arquivo já esta registrado no processo!"
            else:                        
                processoFile = ProcessoFile
                processoFile.add(processoFile)

                # adiciona referencias do arquivo 
                refs = processoFile.conteudo.split('\n')
                linha=1
                for ref in refs:
                    if len(ref.strip())>0:
                        processoFileReferencia = ProcessoFileReferencia()
                        processoFileReferencia.referencia = ref
                        processoFileReferencia.linha = linha
                        processoFileReferencia.processo_file_id = processoFile.id
                        processoFileReferencia.add(processoFileReferencia)
                        linha = linha +1

                self.authentic["code"] = "200"
                self.authentic["msg"] = "Registro efetuado com sucesso!"

        except :
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"
        return self.authentic

    def removerProcesso(self, id):
        try:
            obj = Processo()
            obj = self.processo.query.filter_by(id=id).first()
            obj.delete(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro deletado com sucesso!"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

        return self.authentic

    def removerFile(self, id):
        try:
            obj = ProcessoFile()
            obj = self.processoFile.query.filter_by(id=id).first()
            obj.delete(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro deletado com sucesso!"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

        return self.authentic

    def removerReferencia(self, id):
        try:
            obj = ProcessoFileReferencia()
            obj = self.processoFileReferencia.query.filter_by(id=id).first()
            obj.delete(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro deletado com sucesso!"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"
        return self.authentic

    def buscarReferencias(self, id):
        # try:
        file = self.processoFile.query.filter_by(id=id).first()

        for referencia in file.referencias:
            print(self.referencia.obterReferencia(referencia.referencia))
            # print(referencia.referencia)
        
        self.authentic["code"] = "200"
        self.authentic["msg"] = "Processamento finalizado com sucesso"

        # except:
        #     self.authentic["code"] = "500"
        #     self.authentic["msg"] = "Erro desconhecido"
            
        return self.authentic
