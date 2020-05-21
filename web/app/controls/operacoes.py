import os
import string
import csv

from flask import Flask, Blueprint
from app.model.models import *
from app.controls.utils import *
from app.controls.processamento import *
from sqlalchemy import DateTime, func, desc
from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

operacoes = Blueprint("operacoes", __name__)

class Operacoes():

    def __init__(self):
        self.response = {"code": "", "msg": "", "id": "", "value": "", "superuser": ""}
        self.dashboard = {"processos": 0, "files": 0, "processadas": 0, "pendentes": 0, "referencias": 0, "traduzidas":0, "pendentes":0, "duplicadas":0}
        self.pesquisa = Pesquisa()
        self.processo = Processo()
        self.processoFile = ProcessoFile()
        self.processoFileReferencia = ProcessoFileReferencia()
        self.referencia = Referencia()
        self.processamento = Processamento()

        # logs
        self.homeDir = "../web/app/logs"
        self.logFile = self.homeDir + '/referencia.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

    def obterDashBoard(self):
        processos = self.obterProcessos()    
        files = str(sum(int(processo.getTotalFiles()) for processo in processos)).zfill(4)
        fileReferencias = self.processoFileReferencia.query.all()
        # ---
        referencias = self.referencia.query.all()       

        self.dashboard["processos"] = len(processos)
        self.dashboard["files"] = files
        self.dashboard["pendentes"] = str(len(list(filter(lambda x: x.situacao=='Pendente', fileReferencias)))).zfill(4)
        self.dashboard["processadas"] = str(len(list(filter(lambda x: x.situacao=='Processado', fileReferencias)))).zfill(4)
        self.dashboard["referencias"] = str(len(referencias)).zfill(4)
        # self.dashboard[""] = 0

        return self.dashboard

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

            self.response["code"] = "200"
            self.response["msg"] = "Registro efetuado com sucesso!"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
        return self.response

    def registrarProcessoArquivo(self, ProcessoFile):
        try:
            file = self.processoFile.query.filter_by(name_file=ProcessoFile.name_file, processo_id=ProcessoFile.processo_id).first()
            if file != None:
                self.response["code"] = "500"
                self.response["msg"] = "Arquivo já esta registrado no processo!"
            else:                        
                processoFile = ProcessoFile
                processoFile.add(processoFile)

                # adiciona referencias do arquivo 
                refs = processoFile.conteudo.split('\n')
                linha=1
                for ref in refs:
                    if len(ref.strip())>0:
                        processoFileReferencia = ProcessoFileReferencia()
                        processoFileReferencia.txt_referencia = ref
                        processoFileReferencia.linha = linha
                        processoFileReferencia.processo_file_id = processoFile.id
                        processoFileReferencia.add(processoFileReferencia)
                        linha = linha +1

                self.response["code"] = "200"
                self.response["msg"] = "Registro efetuado com sucesso!"

        except :
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
        return self.response

    def obterProcessoArquivoById(self, id):
        return self.processoFile.query.filter_by(id=id).first()

    def exportarProcessoArquivoById(self, id):
        file = self.processoFile.query.filter_by(id=id).first()
        return list(filter(lambda x : x.situacao=='Processado', file.referencias))  
    
    def removerProcesso(self, id):
        try:
            obj = Processo()
            obj = self.processo.query.filter_by(id=id).first()
            obj.delete(obj)

            self.response["code"] = "200"
            self.response["msg"] = "Registro deletado com sucesso!"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"

        return self.response

    def removerFile(self, id):
        try:
            obj = ProcessoFile()
            obj = self.processoFile.query.filter_by(id=id).first()
            obj.delete(obj)

            self.response["code"] = "200"
            self.response["msg"] = "Registro deletado com sucesso!"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"

        return self.response

    def removerFileReferencia(self, id):
        try:
            obj = ProcessoFileReferencia()
            obj = self.processoFileReferencia.query.filter_by(id=id).first()
            obj.delete(obj)

            self.response["code"] = "200"
            self.response["msg"] = "Registro deletado com sucesso!"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
        return self.response

    def buscarFileReferencias(self, id):
        try:
            file = self.processoFile.query.filter_by(id=id).first()

            logger.debug('----------------------------------------------------------------------------------------------')
            logger.debug('---> Iniciando processo de Extração das Referências.')            

            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

            for referencia in list(filter(lambda x: x.situacao=='Pendente', file.referencias)):
                ref = self.processamento.obterReferencia(referencia.txt_referencia)
                logger.debug('---> {} ---[ work ] extraindo referência [{}]'.format(data_atual, referencia.txt_referencia))
                
                if str(ref).lstrip().__len__() > 0:
                    if ref != 'err':
                        referencia.bibtext = ref
                        referencia.situacao = "Processado"
                        referencia.update()

                        logger.debug('---> {} ---[  ok  ] referência extraída com sucesso! [{}]'.format(data_atual, ref))
                    else:
                        logger.debug('---> {} ---[  erro  ] erro ao tentar acessar processo! [{}]'.format(data_atual, referencia.txt_referencia))
                else:
                    logger.debug('---> {} ---[ erro ] referência não foi extraída [{}]'.format(data_atual, referencia.txt_referencia))

            self.response["code"] = "200"
            self.response["msg"] = "Processamento finalizado com sucesso"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
            
        return self.response

    def obterReferencias(self):
        return self.referencia.query.all()        

    def obterReferenciaById(self, id):
        return self.referencia.query.filter_by(id=id).first()        

    def obterReferenciasBySituacao(self, situacao):
        return self.referencia.query.filter_by(situacao=situacao).all()            

    def importarBibText(self, strBibText):
        try:
            referencias = self.processamento.importarReferencia(strBibText)
            self.referencia.addAll(referencias)

            self.response["code"] = "200"
            self.response["msg"] = "Processamento finalizado com sucesso"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
            
        return self.response

    def atualizarSituacaoReferencia(self, situacaoOld, situacaoNew):
        try:
            referencias = self.referencia.query.filter_by(situacao=situacaoOld).all()            
            for referencia in referencias:
                referencia.situacao = situacaoNew
                referencia.update()

                self.response["code"] = "200"
                self.response["msg"] = "Atualização processada com sucesso"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
            
        return self.response            

    def removerReferencia(self, id):
        try:
            obj = Referencia()
            obj = self.referencia.query.filter_by(id=id).first()
            obj.delete(obj)

            self.response["code"] = "200"
            self.response["msg"] = "Registro deletado com sucesso!"

        except:
            self.response["code"] = "500"
            self.response["msg"] = "Erro desconhecido"
        return self.response        