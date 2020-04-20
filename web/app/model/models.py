import os
import datetime
import sqlalchemy

from enum import Enum
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func
from sqlalchemy.orm import relationship, backref

from werkzeug.security import generate_password_hash, check_password_hash

models = Blueprint("models", __name__)

app = Flask(__name__)
db = SQLAlchemy(app)


# Classe Usuario
class Usuario(db.Model):
    __tablename__ = "usuario"

    # dados pessoais
    id = db.Column(db.Integer, primary_key=True)

    situacao = db.Column(db.String(30), default="Ativa")
    email = db.Column(db.String(100))
    nomecompleto = db.Column(db.String(100))
    sexo = db.Column(db.String(30))
    fonecelular = db.Column(db.String(12))
    dtnascimento = db.Column(db.String(10))

    # endereço
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(60))
    estado = db.Column(db.String(30))
    cep = db.Column(db.String(12))

    # acesso
    senha = db.Column(db.String(30))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())
    superuser = db.Column(db.String(12), default='False')
    token = db.Column(db.String(100))

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def add(self, usuario):
        db.session.add(usuario)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'situacao': self.situacao,
            'email': self.email,
            'nomeCompleto': self.nomecompleto,
            'token': self.token
        }

    def __repr__(self):
        return self.serialize()


# Classe Associado
class Associado(db.Model):
    __tablename__ = "associado"

    # dados essenciais
    id = db.Column(db.Integer, primary_key=True)

    situacao = db.Column(db.String(30), default="Disponivel")
    email = db.Column(db.String(100))
    nomefantasia = db.Column(db.String(100))
    resumo = db.Column(db.String(400))
    tipopessoa = db.Column(db.String(30))
    categoria = db.Column(db.String(60))
    funcionamentodias = db.Column(db.String(50))
    funcionamentohorarioinicio = db.Column(db.String(20))
    funcionamentohorariotermino = db.Column(db.String(20))
    taxaentrega = db.Column(db.String(1), default="N")
    valortaxaentrega = db.Column(db.String(10), default="0,00")
    agenda_entrega = db.Column(db.String(1), default="N")     

    # endereço
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(50))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(60))
    estado = db.Column(db.String(30))
    cep = db.Column(db.String(12))

    # acesso
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())
    logo = db.Column(db.String(100))

    categorias_associado = relationship('AssociadoCategoria', backref='associado')
    avaliacoes = relationship('PedidoAvaliacao', backref='associado')
    
    
    def avaliacao(self):
        count_nota1 = 0
        count_nota2 = 0
        count_nota3 = 0
        count_nota4 = 0
        count_nota5 = 0

        soma_nota1 = 0
        soma_nota2 = 0
        soma_nota3 = 0
        soma_nota4 = 0
        soma_nota5 = 0
        
        if len(self.avaliacoes) == 0:
            return "Novo"
        else:
            # encontra o total de avaliacoes por nota
            for avaliacao in self.avaliacoes:
                if avaliacao.nota ==1:
                    count_nota1 = count_nota1+1
                if avaliacao.nota ==2:
                    count_nota2 = count_nota2+1
                if avaliacao.nota ==3:
                    count_nota3 = count_nota3+1
                if avaliacao.nota ==4:
                    count_nota4 = count_nota4+1
                if avaliacao.nota ==5:
                    count_nota5 = count_nota5+1           
                             
            # multiplica as notas pelos totais encontrados
            soma_nota1 = count_nota1 * 1
            soma_nota2 = count_nota2 * 2
            soma_nota3 = count_nota3 * 3
            soma_nota4 = count_nota4 * 4
            soma_nota5 = count_nota5 * 5
            
            soma = (soma_nota1+soma_nota2+soma_nota3+soma_nota4+soma_nota5)
            avaliacao = (soma_nota1+soma_nota2+soma_nota3+soma_nota4+soma_nota5)/(count_nota1+count_nota2+count_nota3+count_nota4+count_nota5)
                
            return round(avaliacao, 1)
        

    def add(self, associado):
        db.session.add(associado)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'situacao': self.situacao,
            'email': self.email,
            'nomeFantasia': self.nomefantasia,
            'resumo': self.resumo
        }

    def __repr__(self):
        return self.serialize()


# Classe Categorias
class Categoria(db.Model):
    __tablename__ = "categoria"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)
    descricao = db.Column(db.String(60))
    logo = db.Column(db.String(100))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    def serialize(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'logo': self.logo,
            'dtregistro': self.dtregistro
        }

    def __repr__(self):
        return self.serialize()


# Classe associativa AssociadoxCategorias
class AssociadoCategoria(db.Model):
    __tablename__ = "associado_categorias"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    associado_id = db.Column(db.Integer, db.ForeignKey('associado.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    resumo = db.Column(db.String(60))
    logo = db.Column(db.String(100))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    catego = relationship(Categoria, backref=backref(
        "associado_categorias", cascade="all, delete-orphan"))
    assoc = relationship(Associado, backref=backref(
        "associado_categorias", cascade="all, delete-orphan"))
    prods = relationship("Produto", backref='associado_categorias', lazy=False)

    tipos = ["Tradicionais", "Especiais", "Premium", "Doces"]

    def serialize(self):
        return {
            'id': self.id,
            'associado_id': self.associado_id,
            'nomeFantasia': self.assoc.nomefantasia,
            'categoria_id': self.categoria_id,
            'categoria': self.catego.descricao,
            'resumo': self.resumo,
            'logo': self.logo
        }

    def __repr__(self):
        return self.serialize()

# classe Produto


class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column('id', db.Integer, primary_key=True)

    associado_categoria_id = db.Column(db.Integer, db.ForeignKey('associado_categorias.id'))
    descricao = db.Column(db.String(200))
    valor = db.Column(db.String(30))
    tipo = db.Column(db.String(30))
    resumo = db.Column(db.String(400))
    medida = db.Column(db.String(30))
    logo = db.Column(db.String(100))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    tamanhos = relationship('ProdutoTamanho', backref='produto')

    def add(self, produto):
        db.session.add(produto)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'valor': self.valor,
            'tipo': self.tipo,
            'resumo': self.resumo,
            'medida': self.medida,
            'logo': self.logo
        }

    def __repr__(self):
        return self.serialize()


# classe Produto x Preco x Tamanho
class ProdutoTamanho(db.Model):
    __tablename__ = "produto_tamanho"

    id = db.Column('id', db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    tamanho = db.Column(db.String(30))
    valor = db.Column(db.String(30))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    def add(self, produto_tamanho):
        db.session.add(produto_tamanho)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'produto_id': self.produto_id,
            'tamanho': self.tamanho,
            'valor': self.valor
        }

    def __repr__(self):
        return self.serialize()


# Classe associativa UsuarioxAssociadoxTags
class TagAssociado(db.Model):
    __tablename__ = "associado_usuario_tags"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    associado_id = db.Column(db.Integer, db.ForeignKey('associado.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    recomendo = db.Column(db.String(1))
    favorito = db.Column(db.String(1))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    user = relationship(Usuario, backref=backref(
        "associado_usuario_tags", cascade="all, delete-orphan"))
    assoc = relationship(Associado, backref=backref(
        "associado_usuario_tags", cascade="all, delete-orphan"))

    def add(self, tag):
        db.session.add(tag)
        db.session.commit()

    def update(self):
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'nomeCompleto': self.user.nomecompleto,
            'associado_id': self.associado_id,
            'nomeFantasia': self.assoc.nomefantasia,
            'favorito': self.favorito,
            'recomendo': self.recomendo
        }

    def __repr__(self):
        return self.serialize()


# classe Carrinho
class Carrinho(db.Model):
    __tablename__ = "carrinho"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    associado_id = db.Column(db.Integer, db.ForeignKey('associado.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))

    resumo = db.Column(db.String(1000))
    tamanho = db.Column(db.String(30))
    categoria = db.Column(db.String(100))
    valor_unitario = db.Column(db.String(30))
    quantidade = db.Column(db.String(30))
    total_item = db.Column(db.String(30))
    ids = db.Column(db.String(100))
    dtregistro = db.Column(db.DateTime, default=datetime.datetime.today())

    assoc = relationship(Associado, backref=backref("carrinho"))
    prods = relationship(Produto, backref=backref("carrinho"))

    def add(self, carrinho):
        db.session.add(carrinho)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, carrinho):
        db.session.delete(carrinho)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'associado_id': self.associado_id,
            'produto_id': self.produto_id,
            'resumo': self.resumo,
            'tamanho': self.tamanho,
            'valor_unitario': self.valor_unitario,
            'quantidade': self.quantidade
        }

    def __repr__(self):
        return self.serialize()


# classe Pedido
class Pedido(db.Model):
    __tablename__ = "pedido"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    associado_id = db.Column(db.Integer, db.ForeignKey('associado.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    numero = db.Column(db.String(30))
    dtagendamento = db.Column(db.String(30))
    situacao = db.Column(db.String(30))
    total_itens = db.Column(db.String(30))
    taxa_entrega = db.Column(db.String(30))
    total_pedido = db.Column(db.String(30))
    avaliacao_pontos = db.Column(db.String(30))

    avaliacao_comentarios = db.Column(db.String(150))
    motivo_cancelamento = db.Column(db.String(150))
    observacao = db.Column(db.String(150), default="")
    dtregistro = db.Column(db.String(30))

    itens = relationship('PedidoItem', backref=backref("pedido"))
    assoc = relationship(Associado, backref=backref("pedido"))
    user = relationship(Usuario, backref=backref("pedido"))

    def add(self, pedido):
        db.session.add(pedido)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, pedido):
        db.session.delete(pedido)
        db.session.commit()

    @property
    def status(self):
        if self.situacao == "1":
            return "Iniciado"

        if self.situacao == "2":
            return "Em Análise"

        if self.situacao == "3":
            return "Entrega"

        if self.situacao == "4":
            return "Finalizado"

        if self.situacao == "5":
            return "Cancelado"

    def serialize(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'associado_id': self.associado_id,
            'numero': self.numero,
            'situacao': self.situacao,
            'dtagendamento': self.dtagendamento,
            'total_itens': self.total_itens,
            'taxa_entrega': self.taxa_entrega,
            'total_pedido': self.total_pedido,
            'avaliacao_pontos': self.avaliacao_pontos,
            'observacao': self.observacao
        }

    def __repr__(self):
        return self.serialize()


class PedidoItem(db.Model):
    __tablename__ = "pedido_item"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))

    categoria = db.Column(db.String(100))
    resumo = db.Column(db.String(100))
    tamanho = db.Column(db.String(30))
    quantidade = db.Column(db.String(30))
    valor_unitario = db.Column(db.String(30))
    total_item = db.Column(db.String(30))
    ids = db.Column(db.String(100))

    ped = relationship('Pedido', backref=backref("pedido_item"))
    prods = relationship('Produto', backref=backref("pedido_item"))

    def add(self, pedido_item):
        db.session.add(pedido_item)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, pedido_item):
        db.session.delete(pedido_item)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id,
            'produto_id': self.produto_id,
            'categoria': self.categoria,
            'resumo': self.resumo,
            'tamanho': self.tamanho,
            'quantidade': self.quantidade,
            'valor_unitario': self.valor_unitario,
            'total_item': self.total_item,
            'ids': self.ids
        }

    def __repr__(self):
        return self.serialize()



# Classe PedidoAvaliacao
class PedidoAvaliacao(db.Model):
    __tablename__ = "pedido_avaliacao"

    # dados essenciais
    id = db.Column('id', db.Integer, primary_key=True)

    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    associado_id = db.Column(db.Integer, db.ForeignKey('associado.id'))
    comentario = db.Column(db.String(150))
    nota = db.Column(db.Integer)

    date = datetime.datetime.now()
    dtregistro = db.Column(db.String(30))

    def add(self, pedidoAvaliacao):
        db.session.add(pedidoAvaliacao)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'pedido_id': self.pedido_id,
            'associado_id': self.associado_id,
            'comentario': self.comentario,
            'nota': self.nota,
            'dtregistro': self.dtregistro            
        }

    def __repr__(self):
        return self.serialize()
