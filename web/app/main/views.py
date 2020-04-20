import os

from flask import Flask, Blueprint, render_template, session, request, redirect, url_for, send_from_directory, Response
from app.controls.auth import *
from app.controls.operacoes import *
from app.controls.utils import *
from app.model.models import *
from decimal import Decimal

views = Blueprint("views", __name__)
auth = Autenticacao()
oper = Operacoes()

# Classes referentes a autenticação e regsitro no sistema
# ----------------------
@views.route('/', methods=['GET', 'POST'])
def index():
    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        return render_template('login.html', page=None)


@views.route('/home', methods=['GET', 'POST'])
def home():
    if 'email' in session:    
        nome = session.get("nome")
        adm = session.get("superuser")
        pedidos = oper.obterPedidosSemAvaliacao(session.get('id'))
        print(adm)
        return render_template('index.html', nome=nome, pedidos=pedidos, adm=adm)
    else:
        return render_template('login.html', page=None)

@views.route('/logout', methods=['GET'])
def sair():
    session.pop('email', None)
    session.pop('id', None)
    session.pop('nome', None)
    session.pop('token', None)
    session.pop('adm', None)
    session.pop('msg', None)
    session.pop('value', None)
    session.pop('superuser', None)
    return redirect(url_for('views.index'))


@views.route('/validaremail/<email>')
def validar_email(email):
    result = auth.validar_email(email=email)
    return result.get("code")


@views.route('/validarfone/<celular>')
def validar_celular(celular):
    result = auth.validar_celular(celular)
    return result.get("code")


@views.route('/recuperasenha', methods=['GET'])
def recuperar_senha():
    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        return render_template('recuperasenha.html', page=None)


@views.route('/recuperasenha/envio', methods=['POST'])
def enviar_senha():
    result = auth.validar_email(request.form['email-recuperar'])

    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        if result.get("code") != "200":
            # atualizar senha e enviar email
            result = auth.enviar_senha(request.form['email-recuperar'])
            return redirect(url_for('views.recuperar_senha'))
        else:
            return render_template('recuperasenha.html', page=result)


@views.route('/login', methods=['POST'])
def user():
    result = auth.autenticarUsuario(
        request.form['email-login'], request.form['password'])

    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        if request.method == 'POST':
            if result.get("code") == "200":
                session['email'] = result.get("email")
                session['token'] = result.get("token")
                session['nome'] = result.get("nome")
                session['id'] = result.get("id")
                session['superuser'] = result.get("superuser")
                return redirect(url_for('views.home'))
            else:
                return render_template('login.html', page=result)
        else:
            return render_template('login.html', page=result)


@views.route('/registro', methods=['GET'])
def cadastro():
    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        return render_template('registro.html', page=None)


@views.route('/registro/envio', methods=['POST'])
def registrar():
    if 'email' in session:
        return redirect(url_for('views.home'))
    else:
        usuario = Usuario()

        usuario.nomecompleto = request.values.get('nomecompleto')
        usuario.email = request.values.get('email')
        usuario.fonecelular = request.values.get('celular')
        usuario.sexo = request.values.get('sexo')
        usuario.dtnascimento = request.values.get('dtnascimento')
        usuario.cep = request.values.get('cep')
        usuario.logradouro = request.values.get('logradouro')
        usuario.numero = request.values.get('numero')
        usuario.complemento = request.values.get('complemento')
        usuario.bairro = request.values.get('bairro')
        usuario.cidade = request.values.get('cidade')
        usuario.estado = request.values.get('estado')
        usuario.set_password(request.values.get('senha'))

        result = auth.registrarUsuario(usuario)

        return result.get("code")

# Classes referentes a operações
# ----------------------
@views.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)


@views.route('/favorito/associado/<id>')
def registrarFavorito(id):
    result = oper.registrarFavorito(id, session.get("id"))
    return result.get("msg")

@views.route('/associado', methods=['GET'])
@views.route('/associado/<valor>', methods=['GET'])
def carregarAssociados(valor=None):
    if 'email' in session:
        if valor==None:
            associados = oper.obterAssociados()
        else:    
            associados = oper.obterAssociadoByCategorias(valor)    
        
        return render_template('associado.html', associados=associados)

    else:
        return render_template('login.html', page=None)

@views.route('/associado/atualizar', methods=['POST'])
def atualizarAssociado():
    id = request.values.get('id')
    situacao = request.values.get('situacao')

    if 'email' in session:      
        associado = oper.obterAssociadoById(id)
        associado.situacao = situacao
        result = oper.atualizarAssociado(associado)
        print(associado.__str__())
        return result.get("code")

    else:
        return render_template('login.html', page=None)


@views.route('/associado/cardapio/<associado_id>')
def carregar_cardapio(associado_id):
    if 'email' in session:
        associado = oper.obterAssociadoById(associado_id)
        return render_template('cardapio.html', associado=associado)
    else:
        return render_template('login.html', page=None)


@views.route('/associado/categoria/<associado_categoria_id>')
def carregar_cardapio_produtos(associado_categoria_id):
    if 'email' in session:
        associado_categoria = oper.obterAssociadoCategoriaById(
            associado_categoria_id)
        return render_template('cardapio_produtos.html', associado_categoria=associado_categoria)
    else:
        return render_template('login.html', page=None)


@views.route('/produto', methods=['GET'])
def obterProdutoPreco():
    if 'email' in session:
        id = request.args.get('id')
        tamanho = request.args.get('tamanho')

        produto_tamanho = oper.obterPreco(id, tamanho)
        return produto_tamanho.valor
    else:
        return render_template('login.html', page=None)


@views.route('/carrinho', methods=['POST'])
def registrarCarrinho():
    if 'email' in session:
        carrinho = Carrinho()

        carrinho.usuario_id = session.get("id")
        carrinho.produto_id = request.values.get('produto_id')
        carrinho.associado_id = request.values.get('associado_id')
        carrinho.categoria = request.values.get('categoria')
        carrinho.resumo = request.values.get('resumo')
        carrinho.tamanho = request.values.get('tamanho')
        # ------------------------------------------------------------------
        carrinho.quantidade = request.values.get('quantidade')
        carrinho.valor_unitario = request.values.get('valor_unitario')
        carrinho.total_item = str((int(request.values.get('quantidade')) * Decimal(
            request.values.get('valor_unitario')[3:].replace(",", "."))))
        carrinho.ids = request.values.get('ids')

        result = oper.registrarProdutoCarrinho(carrinho)
        return result.get("code")

    else:
        return render_template('login.html', page=None)


@views.route('/carrinho/itens', methods=['GET'])
def obterCarrinho():
    if 'email' in session:
        carrinho = oper.obterCarrinho(session.get("id"))
        return render_template('carrinho.html', carrinho=carrinho)
    else:
        return render_template('login.html', page=None)


@views.route('/carrinho/item', methods=['POST'])
def deleteItemCarrinho():
    id = request.values.get('id')

    if 'email' in session:
        # remove item
        result = oper.deletarItemCarrinho(id)
        return result.get("code")

    else:
        return render_template('login.html', page=None)


@views.route('/carrinho/limpar', methods=['POST'])
def limparCarrinho():
    if 'email' in session:
        # limpa o carrinho
        itens = oper.obterCarrinho(session.get("id"))
        for item in itens:
            result = oper.deletarItemCarrinho(item.id)

        return result.get("code")

    else:
        return render_template('login.html', page=None)

@views.route('/pedido', methods=['GET'])
@views.route('/pedido/<status>', methods=['GET'])
def obterPedidos(status=None):
    if 'email' in session:
        if status==None:
            Pedidos = oper.obterPedidos(session.get('id'))
        else: 
            Pedidos = oper.obterPedidosByStatus(session.get('id'), status)    
        return render_template('pedidos.html', pedidos=Pedidos)

    else:
        return render_template('login.html', page=None)


@views.route('/pedido/atualizar', methods=['POST'])
def atualizarObservacao():
    id = request.values.get('id')
    observacao = request.values.get('observacao')[:149]

    if 'email' in session:
        pedido = oper.obterPedidoById(id)
        pedido.observacao = observacao
        result = oper.atualizarPedido(pedido)

        return result.get("code")

    else:
        return render_template('login.html', page=None)

@views.route('/pedido/cancelar', methods=['POST'])
def atualizarSituacaoCancelado():
    id = request.values.get('id')

    if 'email' in session:      
        pedido = oper.obterPedidoById(id)
        pedido.situacao = "5"
        result = oper.atualizarPedido(pedido)

        return result.get("code")

    else:
        return render_template('login.html', page=None)

@views.route('/pedido/entregar', methods=['POST'])
def atualizarSituacaoEmEntrega():
    id = request.values.get('id')

    if 'email' in session:      
        pedido = oper.obterPedidoById(id)
        pedido.situacao = "3"
        result = oper.atualizarPedido(pedido)

        return result.get("code")

    else:
        return render_template('login.html', page=None)

@views.route('/pedido/encerrar', methods=['POST'])
def atualizarSituacaoEncerrado():
    id = request.values.get('id')

    if 'email' in session:      
        pedido = oper.obterPedidoById(id)
        pedido.situacao = "4"
        result = oper.atualizarPedido(pedido)

        return result.get("code")

    else:
        return render_template('login.html', page=None)

@views.route('/pedido/finalizar', methods=['POST'])
def atualizarSituacaoFinalizado():
    id = request.values.get('id')    
    dtagendamento = request.values.get('dtagendamento')[8:10] + "/" + request.values.get('dtagendamento')[5:7] + "/" + request.values.get('dtagendamento')[0:4]
    dtatual = datetime.datetime.now()
    agenda_entrega = request.values.get('agenda_entrega')

    if 'email' in session:
        pedido = oper.obterPedidoById(id)
        pedido.situacao = "2"
        pedido.dtagendamento = dtagendamento

        if agenda_entrega=="S":            
            # ano/mes/dia
            d1 = datetime.datetime(int(request.values.get('dtagendamento')[0:4]), int(request.values.get('dtagendamento')[5:7]), int(request.values.get('dtagendamento')[8:10])) 
            d2 = datetime.datetime(dtatual.year, dtatual.month, dtatual.day)         
            
            # dtagendamento deve ser maior que a data atual     
            if d1 > d2:
                result = oper.atualizarPedido(pedido)
                return result.get("code")            
            else:    
                return "Data de Agendamento deve ser maior que a Data Atual"
        else:
            result = oper.atualizarPedido(pedido)
            return result.get("code")                            

    else:
        return render_template('login.html', page=None)

@views.route('/pedido/avaliar/<id>', methods=['GET'])
def avaliarPedido(id):
    if 'email' in session:
        pedido = oper.obterPedidoById(id)
        return render_template('pedido_avaliacao.html', pedido=pedido)
    
    else:
        return render_template('login.html', page=None)
     
    
@views.route('/pedido/concluir', methods=['POST'])
def concluirPedido():   
    date = datetime.datetime.now()    
    
    id = request.values.get('id')    
    nota = request.values.get('nota')
    comentario = request.values.get('comentario')
    dtregistro = str(date.day).zfill(2) + "/" + str(date.month).zfill(2) + "/" + str(date.year) + " " + str(date.hour).zfill(2) + ":" + str(date.minute).zfill(2)

    if 'email' in session:
        # registra a avalicao no pedido
        pedido = oper.obterPedidoById(id)
        associado_id = pedido.associado_id
        pedido.avaliacao_pontos = nota
        pedido.avaliacao_comentarios = comentario
 
        result = oper.atualizarPedido(pedido)
        
        # registra a avaliacao do pedido na tabela de avaliacoes      
        pedidoAvaliacao = PedidoAvaliacao()
        pedidoAvaliacao.associado_id = associado_id
        pedidoAvaliacao.pedido_id = id
        pedidoAvaliacao.nota = nota
        pedidoAvaliacao.comentario = comentario
        
        valor = oper.registrarAvaliacao(pedidoAvaliacao)
        
        return result.get("code")                            

    else:
        return render_template('login.html', page=None)
 
    
@views.route('/pedido/gerar', methods=['POST'])
def gerarPedidos():
    if 'email' in session:
        result = oper.gerarPedidos(session.get('id'))

        return result.get("code")

    else:
        return render_template('login.html', page=None)


@views.route('/perfil', methods=['GET'])
def atualizarPerfil():
    if 'email' in session:
        Usuario = auth.obterUsuario(session.get('id'))
        return render_template('perfil.html', Usuario=Usuario, page=None)

    else:
        return render_template('login.html', page=None)

@views.route('/perfil/atualizar', methods=['POST'])
def atualizarUsuario():
    if 'email' in session:
        usuario = Usuario()
        usuario = auth.obterUsuario(session.get('id'))            
        
        usuario.nomecompleto = request.values.get('nomecompleto')
        usuario.fonecelular = request.values.get('celular')
        usuario.sexo = request.values.get('sexo')
        usuario.dtnascimento = request.values.get('dtnascimento')
        usuario.cep = request.values.get('cep')
        usuario.logradouro = request.values.get('logradouro')
        usuario.numero = request.values.get('numero')
        usuario.complemento = request.values.get('complemento')
        usuario.bairro = request.values.get('bairro')
        usuario.cidade = request.values.get('cidade')
        usuario.estado = request.values.get('estado')

        result = auth.atualizarUsuario(usuario)

        return result.get("code")
    
    else:
        return render_template('login.html', page=None)
    
    
@views.route('/perfil/acesso', methods=['POST'])
def atualizarAcesso():
    if 'email' in session:
        usuario = Usuario()
        usuario = auth.obterUsuario(session.get('id'))
                    
        senha_atual = request.values.get('senhaAtual')
        
        if usuario.check_password(senha_atual):            
            usuario.set_password(request.values.get('senha'))        
            result = auth.atualizarUsuario(usuario)

            return result.get("code")
        else:
            return "403"        
    
    else:
        return render_template('login.html', page=None)


@views.route('/dashboard', methods=['GET'])
@views.route('/dashboard/<status>', methods=['GET'])
def carregarDashboard(status=None):
    if 'email' in session:
        usuario = auth.obterUsuario(session.get('id'))
        if usuario.superuser=='True':
            associados = oper.obterAssociados()
            clientes = auth.obterClientes()
                    
            if status==None:
                pedidos = oper.obterTodosPedidos()
            else:
                pedidos = oper.obterPedidosDashboardByStatus(status)    
            
            return render_template('dashboard.html', usuario=usuario, associados=associados, clientes=clientes, pedidos=pedidos)
        else:
            return render_template('login.html', page=None)
    else:
        return render_template('login.html', page=None)
    
@views.route('/dashboard/download', methods=['GET'])    
def gerarDownload():
    if 'email' in session:
        return Response(oper.obterArquivoCSV(), mimetype="text/csv", headers={"Content-disposition":"attachment; filename=dados.csv"})        
    else:
        return render_template('login.html', page=None)            
