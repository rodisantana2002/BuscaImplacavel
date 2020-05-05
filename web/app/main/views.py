import os

from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, send_from_directory, Response
from app.controls.operacoes import *
from app.controls.utils import *
from app.model.models import *
from decimal import Decimal

views = Blueprint("views", __name__)
oper = Operacoes()

# Classes referentes a autenticação e regsitro no sistema
# ----------------------
@views.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('views.home'))


@views.route('/home', methods=['GET', 'POST'])
def home():
    processos = oper.obterProcessos()    
    files = sum(int(processo.getTotalFiles()) for processo in processos)
    refPendentes = 0
    refProcessadas = 0
    return render_template('index.html', processos=processos, files=files, refPendentes=refPendentes, refProcessadas=refProcessadas)


@views.route('/processo', methods=['GET'])
@views.route('/processo/<id>', methods=['GET'])
def carregarProcesso(id=None):
    if id == None:
        processos = oper.obterProcessos()
        return render_template('processos.html', processos=processos)
    else:
        processo = oper.obterProcessoById(id)
        return render_template('processosDetail.html', processo=processo)


@views.route('/processo/registro', methods=['GET', 'POST'])
def carregarFormProcesso():
    if request.method == 'GET':
        return render_template('processosNew.html', page=None)
    else:
        processo = Processo()

        processo.descricao = request.values.get('descricao')
        processo.objetivo = request.values.get('objetivo')
        # ------------------------------------------------------------------
        result = oper.registrarProcesso(processo)
        return result.get("code")


@views.route('/processo/arquivo', methods=['POST'])
def registrarProcessoArquivo():
    file = ProcessoFile()
    file.name_file = request.values.get('name_file')
    file.processo_id = request.values.get('processo_id')
    file.conteudo = request.values.get('conteudo')

    # ------------------------------------------------------------------
    result = oper.registrarProcessoArquivo(file)
    return result.get("code")


@views.route('/processo/remover', methods=['POST'])
def removerProcesso():
    id = request.values.get('id')
    result = oper.removerProcesso(id)

    return result.get("code")


@views.route('/processo/arquivo/remover', methods=['POST'])
def removerProcessoArquivo():
    processo_id = request.values.get('id')
    result = oper.removerFile(processo_id)
    
    return result.get("code")


@views.route('/processo/arquivo/referencia/remover', methods=['POST'])
def removerReferencia():
    referencia_id = request.values.get('id')
    result = oper.removerReferencia(referencia_id)

    return result.get("code")


@views.route('/processo/arquivo/processar', methods=['POST'])
def processarArquivoReferencias():
    file_id = request.values.get('id')
    result = oper.buscarReferencias(file_id)
    return result.get("code")


@views.route('/processo/arquivo/exportar', methods=['GET'])    
def exportarArquivo():
    bibText =""    
    file_id = request.values.get('id')
    file = oper.obterProcessoArquivoById(file_id)
    referencias = oper.exportarProcessoArquivoById(file_id)

    bibText = [ref.bibtext + ", \n"  for ref in referencias]
    return Response(bibText, mimetype="text/txt", headers={"Content-disposition":"attachment; filename=" + file.name_file[:-4] + ".bib"})        