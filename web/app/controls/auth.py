import os
import string

from flask import Flask, Blueprint
from app.model.models import Usuario
from random import randrange
from app.controls.utils import *

auth = Blueprint("auth", __name__)

class Autenticacao():
    def __init__(self):
        self.usuario = Usuario()
        self.authentic = {"code": "", "msg": "", "email": "", "token":"", "nome":"", "id": "", "value":"", "superuser":""}
        self.alphabets = string.digits + string.ascii_letters

    def autenticarUsuario(self, email, password):
        try:
            user = self.usuario.query.filter_by(email=email).first()
            if user == None:
                self.authentic["code"] = "404"
                self.authentic["msg"] = "Email não foi localizado!"
            else:
                if user.check_password(password):
                    # registra o token 
                    user.token = self.gerar_string(50)
                    user.update()
                    self.authentic["code"] = "200"
                    self.authentic["msg"] = "OK"
                    self.authentic["email"] = user.email
                    self.authentic["token"] = user.token
                    self.authentic["nome"] = user.nomecompleto
                    self.authentic["id"] = user.id
                    self.authentic["superuser"] = user.superuser
                
                else:
                    self.authentic["code"] = "404"
                    self.authentic["msg"] = "Senha informada esta incorreta!"

        except Exception as e:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido - {}".format(e)

        return self.authentic

    def registrarUsuario(self, usuario):
        # validar se usuario já existe
        user = self.usuario.query.filter_by(email=usuario.email).first()
        if user != None:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Ops! Não foi possível efetivar o registro, pois o Email já esta registrado para outro usuário!"
            return self.authentic

        # validar se celular já existe
        user = self.usuario.query.filter_by(
            fonecelular=usuario.fonecelular).first()
        if user != None:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Ops! Não foi possível efetivar o registro, pois o Telefone celular já esta registrado para outro usuário!"
            return self.authentic

        self.usuario.add(usuario)
        self.authentic["code"] = "200"
        self.authentic["msg"] = "Registro efetuado com sucesso!"
        return self.authentic
    
    def atualizarUsuario(self, usuario):
        try:
            self.usuario = usuario
            self.usuario.update()

            self.authentic["code"] = "200"
            self.authentic["msg"] = "Registro atualizado com sucesso!"
            return self.authentic

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"    

    def obterUsuario(self, id):
        return self.usuario.query.filter_by(id=id).first()
    
    def obterClientes(self):
        return self.usuario.query.order_by(Usuario.nomecompleto).all()
    
    def enviar_senha(self, email):
        try:
            # localiza o usuario    
            user = self.usuario.query.filter_by(email=email).first()                      
            
            # criar senha provisória e atualiza
            senha = self.gerar_string(8)
            user.set_password(senha)
            user.update()

            # envia senha criada
            send = Utils()
            send.send_mail(current_app, "Recuperação de Senha", email, 'mails/send_email.html', user.nomecompleto, senha)        
            
            # prepara o retorn
            self.authentic["code"] = "200"
            self.authentic["msg"] = "Email enviado com sucesso!"        

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"
            
        return self.authentic

    def validar_email(self, email):
        try:
            user = self.usuario.query.filter_by(email=email).first()
            if user != None:
                self.authentic["code"] = "404"
                self.authentic["msg"] = "Email foi localizado!"
            else:
                self.authentic["code"] = "200"
                self.authentic["msg"] = "Email não foi localizado"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

        return self.authentic
    
    def validar_celular(self, celular):
        try:
            user = self.usuario.query.filter_by(fonecelular=celular).first()
            if user != None:
                self.authentic["code"] = "404"
                self.authentic["msg"] = "Celular foi localizado!"
            else:
                self.authentic["code"] = "200"
                self.authentic["msg"] = "Celular não foi localizado"

        except:
            self.authentic["code"] = "500"
            self.authentic["msg"] = "Erro desconhecido"

        return self.authentic

    def gerar_string(self, n):
        return ''.join(self.alphabets[randrange(len(self.alphabets))] for i in range(n))
    
    def eferuar_logout(self):
        pass