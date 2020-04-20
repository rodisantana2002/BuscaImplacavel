import os
import sqlalchemy

from datetime import datetime
from enum import Enum

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from werkzeug.security import generate_password_hash, check_password_hash

models = Blueprint("models", __name__)

app = Flask(__name__)
db = SQLAlchemy(app)

# ---------------------------------------------------------------------------
# Classe Pesquisa
# ---------------------------------------------------------------------------


class Pesquisa(db.Model):
    __tablename__ = 'Pesquisa'
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')

    id = db.Column(db.Integer, primary_key=True)
    situacao = db.Column(db.String(20), default="Ativa")
    descricao = db.Column(db.String(100))
    objetivo = db.Column(db.String(300))
    criado_em = db.Column(db.String(20), default=data_atual)

    referencias = relationship("Referencia", back_populates="pesquisas")

    def add(self, pesquisa):
        db.session.add(pesquisa)
        db.session.commit()

    def addAll(self, pesquisas):
        db.session.add_all(pesquisas)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'situacao': self.situacao,
            'descricao': self.descricao,
            'objetivo': self.objetivo,
            'criado_em': self.criado_em
        }

    def __repr__(self):
        return self.serialize()


# ---------------------------------------------------------------------------
# Classe Referencia
# ---------------------------------------------------------------------------
class Referencia(db.Model):
    __tablename__ = 'Referencia'
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')

    id = db.Column(db.Integer, primary_key=True)
    situacao = db.Column(db.String(20), default="Iniciada")
    titulo = db.Column(db.String(1000))
    resumo = db.Column(db.String())
    ano = db.Column(db.String(10))
    autores = db.Column(db.String(1000))
    keywords = db.Column(db.String(1000))
    doi = db.Column(db.String(300))
    url = db.Column(db.String(300))
    publisher = db.Column(db.String(200))
    bookTitulo = db.Column(db.String(1000))
    arquivo_origem = db.Column(db.String(200))
    pesquisa_id = db.Column(db.Integer, db.ForeignKey('Pesquisa.id'))
    texto_rtf = db.Column(db.String())
    referencia = db.Column(db.String())
    criado_em = db.Column(db.String(20), default=data_atual)
    


    # relacionamentos
    pesquisas = relationship("Pesquisa", back_populates="referencias")
    translates = relationship("Translate")

    def add(self, referencia):
        db.session.add(referencia)
        db.session.commit()

    def addAll(self, referencias):
        db.session.add_all(referencias)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'ano': self.ano,
            'titulo': self.titulo,
            'publisher': self.publisher,
            'doi': self.doi,
            'pesquisa_id': self.pesquisa_id,
            'situacao': self.situacao,
            'resumo': self.resumo,
            'autores': self.autores,
            'keywords': self.keywords,
            'url': self.url,
            'bookTitulo': self.bookTitulo,
            'arquivo_origem': self.arquivo_origem,
            'texto_rtf': self.texto_rtf,
            'referencia': self.referencia,
            'criado_em': self.criado_em
        }

    def __repr__(self):
        return self.serialize()


# ---------------------------------------------------------------------------
# Classe Translate
# ---------------------------------------------------------------------------
class Translate(db.Model):
    __tablename__ = 'Translate'

    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10))
    situacao = db.Column(db.String(20), default="Pendente")
    linha_pos = db.Column(db.Integer)
    txt_origem = db.Column(db.String())
    txt_translate = db.Column(db.String())
    referencia_id = db.Column(db.Integer, db.ForeignKey('Referencia.id'))
    criado_em = db.Column(db.String(20), default=data_atual)

    def add(self, translate):
        db.session.add(translate)
        db.session.commit()

    def addAll(self, translate):
        db.session.add_all(translate)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'linha_pos': self.linha_pos,
            'tipo': self.tipo,
            'situacao': self.situacao,
            'txt_origem': self.txt_origem,
            'txt_translate': self.txt_translate,
            'referencia_id': self.referencia_id,
            'criado_em': self.criado_em
        }

    def __repr__(self):
        return self.serialize()


# ---------------------------------------------------------------------------
# Teste de Classe
# ---------------------------------------------------------------------------
def main():
    pass

    # linha.add(linha)


if __name__ == '__main__':
    main()
