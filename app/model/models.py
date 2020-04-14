import os
import datetime
import sqlalchemy
import lista as list
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///../buscaimplacavel/bases/database/bot.db')        
Session = sessionmaker(bind=engine)
session = Session()   

# ---------------------------------------------------------------------------
# Classe Pesquisa
# ---------------------------------------------------------------------------
class Pesquisa(Base):
    __tablename__ = 'Pesquisa'
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')  
     
    id = Column(Integer, primary_key=True)
    situacao = Column(String(20), default="Ativa")
    descricao = Column(String(100))
    objetivo = Column(String(300))
    criado_em = Column(String(20), default=data_atual)
    
    referencias = relationship("Referencia", back_populates="pesquisas")
    
    
    def add(self, pesquisa):   
        session.add(pesquisa)
        session.commit()    
        
    def addAll(self, pesquisas):
        session.add_all(pesquisas)
        
    def update(self):
        session.commit()
        
    def find_by_id(self, id):
        pesq =  session.query(Pesquisa).filter_by(id=id)
        self = pesq[0]
        print(self.__str__())

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
class Referencia(Base):
    __tablename__ = 'Referencia'
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')  
     
    id = Column(Integer, primary_key=True)
    situacao = Column(String(20), default="Ativa")
    titulo = Column(String(1000))
    resumo = Column(String())
    ano = Column(String(10))
    autores = Column(String(1000))
    keywords = Column(String(1000))
    doi = Column(String(300))
    url = Column(String(300))
    publisher = Column(String(200))
    bookTitulo = Column(String(1000))
    arquivo_origem = Column(String(200))
    pesquisa_id = Column(Integer, ForeignKey('Pesquisa.id'))
    texto_rtf = Column(String())
    criado_em = Column(String(20), default=data_atual)
    
    # relacionamentos
    pesquisas = relationship("Pesquisa", back_populates="referencias")    
    translates = relationship("Translate")
    
    
        
    def add(self, referencia):   
        session.add(referencia)
        session.commit()    
        
    def addAll(self, referencias):
        session.add_all(referencias)
        
    def update(self):
        self.session.commit()
        
    def find_by_id(self, id):
        pesq =  session.query(Referencia).filter_by(id=id)
        self = pesq[0]
        return self

    def serialize(self):
        return {
            'id': self.id,
            'ano': self.ano,
            'titulo': self.titulo,
            'publisher': self.publisher,
            'doi': self.doi,
            'pesquisa_id': self.pesquisa_id,
            'pesquisa': self.pesquisas.descricao,
            'criado_em': self.criado_em
        }

    def __repr__(self):
       return self.serialize()        




# ---------------------------------------------------------------------------
# Classe Translate
# ---------------------------------------------------------------------------
class Translate(Base):
    __tablename__ = 'Translate'
    
    data_hora = datetime.now()
    data_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')  
     
    id = Column(Integer, primary_key=True)
    tipo = Column(String(10))
    situacao = Column(String(20), default="Pendente")
    linha_pos = Column(Integer)
    txt_origem = Column(String())
    txt_translate = Column(String())
    referencia_id = Column(Integer, ForeignKey('Referencia.id'))
    criado_em = Column(String(20), default=data_atual)
    
    def add(self, translate):   
        session.add(translate)
        session.commit()    
        
    def addAll(self, translate):
        session.add_all(translate)
        
    def update(self):
        self.session.commit()
        
    def find_by_id(self, id):
        pesq =  session.query(Translate).filter_by(id=id)
        self = pesq[0]
        return self

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
    # pesquisa = Pesquisa()
    # pesquisa.descricao="Rodolfo"
    # pesquisa.situacao="rr"
    # pesquisa.add(pesquisa)
    # pesquisa.objetivo="meut "    
    # pesquisa = pesquisa.find_by_id(3)
    # print(pesquisa.__str__())
    
    # ref = Referencia()
    # ref.ano = 2019
    # ref.bookTitulo = "bookTitulo"
    # ref.keywords = "key"
    # ref.resumo = "resumo"
    # ref.publisher = "publisher"
    # ref.texto_rtf = "titulo"
    # ref.titulo = "titulo"
    # ref.autores = "Rodolfo e Ines"
    # ref.doi = "19545454"
    # ref.arquivo_origem = "arquivo origem"
    # ref.pesquisa_id = 1
    # ref.url = "url"
    # ref.add(ref)
    
    # ref = ref.find_by_id(5)
    # print(ref.__str__())

    linha = Translate() 
    linha.linha_pos = 1
    linha.tipo ="ABS"
    linha.txt_origem = "origem"
    linha.txt_translate = "translate"
    linha.referencia_id = 1
    linha.add(linha)
    


    
    
if __name__ == '__main__':
    main()        