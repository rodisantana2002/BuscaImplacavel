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
    pesquisa = oper.obterPesquisas()    
    return render_template('index.html', pesquisa=pesquisa)


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
    print(request.values.get('conteudo'))

    # ------------------------------------------------------------------
    result = oper.registrarProcessoArquivo(file)
    return result.get("code")

# @views.route('/pedido', methods=['GET'])
# @views.route('/pedido/<status>', methods=['GET'])
# def obterPedidos(status=None):
#     if 'email' in session:
#         if status == None:
#             Pedidos = oper.obterPedidos(session.get('id'))
#         else:
#             Pedidos = oper.obterPedidosByStatus(session.get('id'), status)
#         return render_template('pedidos.html', pedidos=Pedidos)

#     else:
#         return render_template('login.html', page=None)
