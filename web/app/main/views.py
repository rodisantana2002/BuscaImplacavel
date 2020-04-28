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


@views.route('/processo', methods=['GET', 'POST'])
def carregarProcessos():
    processos = oper.obterProcessos()
    return render_template('processos.html', processos = processos)


@views.route('/processo/<id>')
def carregarProcessoDetail(id):
    processo = oper.obterProcessoById(id)
    return render_template('processosDetail.html', processo=processo)
