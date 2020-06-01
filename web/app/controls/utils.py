import os
import sys
import csv
import sqlite3


from flask import render_template, current_app, Blueprint
from threading import Thread
from flask_mail import Message, Mail


class Utils():
    def __init__(self):
        self.mail = None
    
    def async_send_mail(self, app, msg):
        self.mail = Mail(app)
        with app.app_context():
            self.mail.send(msg)

    def send_mail(self, app, subject, recipient, template, name, senha):
        msg = Message(subject, sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
        msg.html = render_template(template, name=name, senha=senha)

        thr = Thread(target=self.async_send_mail, args=[current_app._get_current_object(), msg])
        thr.start()

        return thr

    def _obterArquivos(self, path, tipo):    
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith(tipo)])


    # Permite a exportação dos dados de quaquer tabela ou consulta do banco de dados
    def gerarCSV(self, path_db, path_arquivo, name, strSQL):
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        columns=[]
        
        # popula os names das colunas
        result = cursor.execute(strSQL)   
        columns = [i[0] for i in result.description]
        line = dict.fromkeys(columns)

        with open(path_arquivo+name+'.csv', 'w') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=columns)
            writer.writeheader()

            # carrega os valores das colunas        
            for row in result:
                col = 0
                # atualiza dicionario e grava como linha no csv
                for key in line.keys():
                    line[key]= str(row[col])
                    col = col+1
                writer.writerow(line)
                
        arquivo.close()    
        print('Arquivo gerado com sucesso--> '+ name)  