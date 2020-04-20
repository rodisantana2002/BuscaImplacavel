import os
import string
import csv

from flask import Flask, Blueprint
from app.model.models import *
from app.controls.utils import *
from sqlalchemy import DateTime, func
from decimal import Decimal

operacoes = Blueprint("operacoes", __name__)

class Operacoes():

    def __init__(self):
        self.authentic = {"code": "", "msg": "", "email": "", "token": "", "nome": "", "id": "", "value": "", "superuser":""}
        self.associado = Associado()
        self.tags = TagAssociado()
        self.associado_categoria = AssociadoCategoria()
        self.produtoTamanho = ProdutoTamanho()
        self.carrinho = Carrinho()
        self.pedido = Pedido()
        self.pedido_item = PedidoItem()
        self.pedido_avaliacao = PedidoAvaliacao()
        self.destino = 'app/bd/dados.csv' 
        self.FIELD_NAMES = ['pedido_id',
                            'numero',
                            'situacao',
                            'vendedor_id',
                            'vendedor_nomefantasia',
                            'agenda_entrega',
                            'total_itens',
                            'taxa_entrega',
                            'total_pedido',
                            'observacao',
                            'avaliacao_pontos',
                            'avaliacao_comentarios',
                            'item_id',
                            'produto_id',    
                            'produto_descricao',
                            'resumo',
                            'categoria',                            
                            'tamanho',
                            'quantidade',
                            'medida',
                            'valor_unitario',
                            'total_item',
                            'ids',
                            'cliente_id',
                            'cliente_nome',
                            'cliente_email',
                            'cliente_fone',
                            'cliente_logradouro',
                            'cliente_numero',
                            'cliente_complemento',
                            'cliente_bairro',
                            'cliente_cidade',
                            'cliente_estado',
                            'cliente_cep'
                            ]                    
        
    def obterAssociados(self):
        return self.associado.query.order_by(Associado.nomefantasia).all()

    def obterAssociadoById(self, valor):
        return self.associado.query.filter_by(id=valor).first()

    def obterAssociadoCategoriaById(self, valor):
        return self.associado_categoria.query.filter_by(id=valor).first()

    def obterAssociadosByNomeResumo(self, valor):
        return self.associado.query.filter(Associado.nomefantasia.contains(valor.upper()) | Associado.resumo.contains(valor.lower())).all()
    
    def obterAssociadoByCategorias(self, categorias):
        return self.associado.query.filter(Associado.categorias_associado.any(AssociadoCategoria.categoria_id.in_([categorias]))).all()
    
    def atualizarAssociado(self, associado):
        try:
            self.associado = associado
            self.associado.update()

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro atualizado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"        

    def obterTagsAssociadoByUser(self, usuario_id):
        return self.tags.query.filter_by(usuario_id=usuario_id).all()

    def registrarFavorito(self, associado_id, usuario_id):
        # validar se a Tag existe
        try:
            obj = TagAssociado()
            obj = self.tags.query.filter_by(
                associado_id=associado_id, usuario_id=usuario_id).first()

            if obj != None:
                obj.favorito = "S"
                obj.update()
            else:
                obj = TagAssociado()
                obj.associado_id = associado_id
                obj.usuario_id = usuario_id
                obj.recomendo = "N"
                obj.favorito = "S"

                self.tags.add(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro efetuado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

    def obterPreco(self, produto_id, tamanho):
        return self.produtoTamanho.query.filter_by(produto_id=produto_id, tamanho=tamanho).first()

    def registrarProdutoCarrinho(self, Produto):
        try:
            obj = Carrinho()

            obj.add(Produto)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro efetuado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

    def obterCarrinho(self, usuario_id):
        return self.carrinho.query.filter_by(usuario_id=usuario_id).all()

    def deletarItemCarrinho(self, id):
        try:
            obj = Carrinho()
            obj = self.carrinho.query.filter_by(id=id).first()
            obj.delete(obj)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro deletado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

    def obterPedidos(self, usuario_id):
        return self.pedido.query.filter_by(usuario_id=usuario_id).order_by(Pedido.numero.desc()).all()

    def obterTodosPedidos(self):
        status = ['2','3']
        return self.pedido.query.filter(Pedido.situacao.in_(status)).order_by(Pedido.numero.desc()).all()

    def obterPedidosByStatus(self, usuario_id, status):
        lst = []
        lst.append(usuario_id)
        return self.pedido.query.filter(Pedido.usuario_id.in_(lst), Pedido.situacao.in_(status)).order_by(Pedido.numero.desc()).all()

    def obterPedidosDashboardByStatus(self, status):
        return self.pedido.query.filter(Pedido.situacao.in_(status)).order_by(Pedido.numero.desc()).all()

    def obterPedidosSemAvaliacao(self, usuario_id):
        return self.pedido.query.filter_by(usuario_id=usuario_id, situacao='4', avaliacao_pontos=None).order_by(Pedido.numero.desc()).all()

    def obterPedidoById(self, id):
        return self.pedido.query.filter_by(id=id).first()

    def atualizarPedido(self, pedido):
        try:
            self.pedido = pedido
            self.pedido.update()

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro atualizado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

    def gerarPedidos(self, usuario_id):
        # deve gerar 1 pedido por associado localizado no carrinho
        associados = set()
        carrinho_itens = []
        date = datetime.datetime.now()

        try:
            carrinho_itens = self.carrinho.query.filter_by(
                usuario_id=usuario_id).all()

            # verifica quando associados estao presentes nos produtos do carrinho
            for item in carrinho_itens:
                associados.add(self.associado.query.filter_by(
                    id=item.associado_id).first())

            # gerar pedido para cada associado encontrado
            for associado in associados:
                pedido = Pedido()
                total_produtos = 0

                for item in carrinho_itens:
                    if item.associado_id == associado.id:
                        total_produtos = total_produtos + \
                            Decimal(item.total_item).quantize(
                                Decimal('.01'), rounding='ROUND_UP')

                txEntrega = Decimal(associado.valortaxaentrega.replace(
                    ",", ".")).quantize(Decimal('.01'), rounding='ROUND_UP')
                total_pedido = total_produtos + txEntrega

                pedido.numero = str(date.year)[2:] + str(date.month).zfill(2) + str(date.day).zfill(2) + str(date.hour) + str(date.minute) + str(date.second) + str(associado.id) + str(usuario_id)
                pedido.dtregistro = str(date.day).zfill(2) + "/" + str(date.month).zfill(2) + "/" + str(date.year) + " " + str(date.hour).zfill(2)  + ":" + str(date.minute).zfill(2) 
                
                pedido.associado_id = associado.id
                pedido.usuario_id = usuario_id
                pedido.situacao = "1"

                pedido.total_itens = str(total_produtos)
                pedido.taxa_entrega = str(txEntrega)
                pedido.total_pedido = str(total_pedido)
                pedido.add(pedido)

                # grava os itens do pedido
                for item in carrinho_itens:
                    if item.associado_id == associado.id:
                        pedidoItem = PedidoItem()
                        pedidoItem.pedido_id = pedido.id
                        pedidoItem.produto_id = item.produto_id
                        pedidoItem.categoria = item.categoria
                        pedidoItem.tamanho = item.tamanho
                        pedidoItem.resumo = item.resumo
                        pedidoItem.quantidade = item.quantidade
                        pedidoItem.valor_unitario = item.valor_unitario
                        pedidoItem.total_item = item.total_item
                        pedidoItem.ids = item.ids

                        pedidoItem.add(pedidoItem)

            # limpa dados do carrinho
            for item in carrinho_itens:
                self.deletarItemCarrinho(item.id)

            # pedido e itens salvos com sucesso
            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro efetuado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"
            
    def registrarAvaliacao(self, pedidoAvaliacao):
        try:
            obj = PedidoAvaliacao()
            obj.add(pedidoAvaliacao)

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro efetuado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"        
            
    def obterArquivoCSV(self):                       
        with open(self.destino, 'w+') as source:
            writer = csv.DictWriter(source, fieldnames=self.FIELD_NAMES)
            writer.writeheader()
            pedidos = self.obterPedidosDashboardByStatus(['2','3','4','5'])
            
            for pedido in pedidos:
                for item in pedido.itens:
                    writer.writerow({'pedido_id': item.ped.id,
                                    'numero': item.ped.numero,
                                    'situacao': item.ped.status,
                                    'vendedor_id': item.ped.assoc.id,
                                    'vendedor_nomefantasia': item.ped.assoc.nomefantasia,
                                    'agenda_entrega':item.ped.assoc.agenda_entrega,
                                    'total_itens': item.ped.total_itens,
                                    'taxa_entrega': item.ped.taxa_entrega,
                                    'total_pedido': item.ped.total_pedido,
                                    'observacao': item.ped.observacao,
                                    'avaliacao_pontos': item.ped.avaliacao_pontos,
                                    'avaliacao_comentarios': item.ped.avaliacao_comentarios,
                                    'item_id': item.id,
                                    'produto_id': item.produto_id,    
                                    'produto_descricao': item.prods.descricao,    
                                    'resumo': item.resumo,
                                    'categoria': item.categoria,                                    
                                    'tamanho': item.tamanho,
                                    'quantidade': item.quantidade,
                                    'medida':item.prods.medida,
                                    'valor_unitario': item.valor_unitario,
                                    'total_item': item.total_item,
                                    'ids': item.ids,
                                    'cliente_id': item.ped.user.id,
                                    'cliente_nome': item.ped.user.nomecompleto,
                                    'cliente_email': item.ped.user.email,
                                    'cliente_fone': item.ped.user.fonecelular,
                                    'cliente_logradouro':item.ped.user.logradouro,
                                    'cliente_numero':item.ped.user.numero,
                                    'cliente_complemento':item.ped.user.complemento,
                                    'cliente_bairro': item.ped.user.bairro,
                                    'cliente_cidade': item.ped.user.cidade,
                                    'cliente_estado': item.ped.user.estado,
                                    'cliente_cep': item.ped.user.cep                                    
                                })
                                
        with open(self.destino) as fp:
            arq_csv = fp.read()
        
        return arq_csv