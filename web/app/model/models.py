import os
import sqlalchemy
import datetime

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

    id = db.Column(db.Integer, primary_key=True)
    situacao = db.Column(db.String(20), default="Ativa")
    descricao = db.Column(db.String(100))
    objetivo = db.Column(db.String(300))
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))


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
# Classe Processo
# ---------------------------------------------------------------------------
class Processo(db.Model):
    __tablename__ = 'Processo'    

    id = db.Column(db.Integer, primary_key=True)
    situacao = db.Column(db.String(20), default="Pendente")
    descricao = db.Column(db.String(100))
    objetivo = db.Column(db.String(300))
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))

    files = relationship('ProcessoFile')

    def getTotalFiles(self):
        return str(len(self.files)).zfill(4)        

    def add(self, processo):
        db.session.add(processo)
        db.session.commit()

    def addAll(self, processos):
        db.session.add_all(processos)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, processo):
        for file in processo.files:    
            file.delete(file)
            
        db.session.delete(processo)
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
# Classe ProcessoFile
# ---------------------------------------------------------------------------
class ProcessoFile(db.Model):
    __tablename__ = 'ProcessoFile'

    id = db.Column(db.Integer, primary_key=True)
    name_file = db.Column(db.String(150))
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))
    processo_id = db.Column(db.Integer, db.ForeignKey('Processo.id'))    
    conteudo = db.Column(db.String())
    # ----------------
    referencias = relationship('ProcessoFileReferencia')

    def getTotalRefPendentes(self):
        return len(list(filter(lambda x: x.situacao=='Pendente', self.referencias)))

    def getTempoProcessamento(self):
        totLinhas = len(list(filter(lambda x: x.situacao=='Pendente', self.referencias)))
                   
        totHoras = totLinhas // 60
        totMinutos = totLinhas % 60
        return '{}h:{}m'.format(str(totHoras).zfill(2), str(totMinutos).zfill(2))

    def add(self, processoFile):
        db.session.add(processoFile)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, processoFile):
        for referencia in processoFile.referencias:
            referencia.delete(referencia)

        db.session.delete(processoFile)    
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name_file,
            'processo_id': self.processo_id,
            'criado_em': self.criado_em
        }

    def __repr__(self):
        return self.serialize()


# ---------------------------------------------------------------------------
# Classe ProcessoFileReferencia
# ---------------------------------------------------------------------------
class ProcessoFileReferencia(db.Model):
    __tablename__ = 'ProcessoFileReferencia'

    id = db.Column(db.Integer, primary_key=True)
    situacao = db.Column(db.String(20), default="Pendente") 
    linha = db.Column(db.Integer)
    referencia = db.Column(db.String())
    bibtext = db.Column(db.String())
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))
    processo_file_id = db.Column(db.Integer, db.ForeignKey('ProcessoFile.id'))
    
    def add(self, Referencia):
        db.session.add(Referencia)
        db.session.commit()

    def addAll(self, Referencias):
        db.session.add_all(Referencias)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete (self, Referencia):
        db.session.delete(Referencia)
        db.session.commit()
    
    def serialize(self):
        return {
            'id': self.id,
            'situacao': self.situacao,
            'linha': self.linha,
            'referncia': self.referencia,
            'bibtext': self.bibtext,
            'processo_file_id': self.processo_id,
            'criado_em': self.criado_em
        }

    def __repr__(self):
        return self.serialize()


# ---------------------------------------------------------------------------
# Classe Referencia
# ---------------------------------------------------------------------------
class Referencia(db.Model):
    __tablename__ = 'Referencia'

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
    texto_rtf = db.Column(db.String())
    referencia = db.Column(db.String())
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))
    
    # relacionamentos
    translates = relationship("Translate")

    def add(self, referencia):
        db.session.add(referencia)
        db.session.commit()

    def addAll(self, referencias):
        db.session.add_all(referencias)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, referencia):
        db.session.delete(referencia)
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

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10))
    situacao = db.Column(db.String(20), default="Pendente")
    linha_pos = db.Column(db.Integer)
    txt_origem = db.Column(db.String())
    txt_translate = db.Column(db.String())
    referencia_id = db.Column(db.Integer, db.ForeignKey('Referencia.id'))
    criado_em = db.Column(db.String(20), default=datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S'))

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
    pro = Processo()
    pro.descricao = "ssd"
    pro.objetivo = "teste"

    pro.add(pro)

    # linha.add(linha)


if __name__ == '__main__':
    main()
