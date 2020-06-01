import sys
import sqlite3
import os
import logging
import csv

from sqlite3 import Error
from sqlalchemy import create_engine

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

class database(object):
    def __init__(self):
        self.pathOrigem = 'sqlite:///../buscaimplacavel/web/app/bd/bot.db' 
        self.pathCSV = '../buscaimplacavel/bases/origem/' 
        self.engine = create_engine(self.pathOrigem)        

    def gerarTabelas(self):
        tabelas = []        
        # tabelas.append("""CREATE TABLE Pesquisa (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                         situacao VARCHAR(20),
        #                                         descricao VARCHAR(30), 
        #                                         objetivo TEXT,
        #                                         criado_em VARCHAR(20));""")

        # tabelas.append("""CREATE TABLE Processo (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                         situacao VARCHAR(20),
        #                                         descricao VARCHAR(150), 
        #                                         objetivo TEXT,
        #                                         criado_em VARCHAR(20));""")                                              

        # tabelas.append("""CREATE TABLE ProcessoFile (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                         name_file VARCHAR(150), 
        #                                         processo_id INTEGER,
        #                                         conteudo TEXT,  
        #                                         criado_em VARCHAR(20));""")                                              

        # tabelas.append("""CREATE TABLE ProcessoFileReferencia (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                         situacao VARCHAR(20),
        #                                         linha INTEGER,                                                
        #                                         txt_referencia TEXT,
        #                                         bibtext TEXT,
        #                                         processo_file_id INTEGER,
        #                                         criado_em VARCHAR(20));""")                                              

        tabelas.append("""CREATE TABLE Referencia (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                situacao VARCHAR(20),
                                                title TEXT,
                                                titulo TEXT, 
                                                ano VARCHAR(4), 
                                                autores TEXT, 
                                                abstract TEXT,
                                                resumo TEXT, 
                                                keywords TEXT, 
                                                doi TEXT, 
                                                url TEXT, 
                                                publisher TEXT,
                                                bookTitulo TEXT, 
                                                criado_em VARCHAR(20));""")

        # tabelas.append("""CREATE TABLE Translate (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                                situacao VARCHAR(20),
        #                                                tipo VARCHAR(10),
        #                                                linha_pos INTEGER,
        #                                                txt_origem TEXT, 
        #                                                txt_translate TEXT, 
        #                                                referencia_id VARCHAR(50),
        #                                                criado_em VARCHAR(12));""")

        # tabelas.append("""CREATE TABLE ReferenciaTag (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                               tag TEXT, 
        #                                               referencia_id VARCHAR(50),
        #                                               criado_em VARCHAR(12));""")

        # tabelas.append("""CREATE TABLE ReferenciaHistorico (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        #                                                     historico TEXT, 
        #                                                     referencia_id VARCHAR(50),
        #                                                     criado_em VARCHAR(12));""")



        for tabela in tabelas:
            self._criarTabela(tabela)

    def _criarTabela(self, strSQL):             
        try:
            with self.engine.connect() as connection:
                result = connection.execute(strSQL)
                print(result)
            logger.debug("tabela criada com sucesso")
        except Error as e:
            logger.debug(e)
   
    def salvarArtigoElemento(self):
        pass    

    def salvarReferencias(self):
        pass    

    def _obterArquivos(self, path, tipo):
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith("." + tipo)])


    # Permite a exportação dos dados de quaquer tabela ou consulta do banco de dados
    def gerarCSV(self, name, strSQL):
        conn = sqlite3.connect("/home/osboxes/Documentos/projetos/automator/buscaimplacavel/web/app/bd/bot.db")
        cursor = conn.cursor()
        columns=[]
        
        # popula os names das colunas
        result = cursor.execute(strSQL)   
        columns = [i[0] for i in result.description]
        line = dict.fromkeys(columns)

        with open(self.pathCSV+name+'.csv', 'w') as arquivo:
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


def main():
    db = database()
    # gerar Tabelas
    # db.gerarTabelas()

    # exporta dados específicos direto do BD
    strSQL = """SELECT  doi as Identifier,
                        titulo as Title, 
                        ano as Year, 
                        autores as Author, 
                        doi as DOI, 
                        url as URL, 
                        keywords as Custom3, 
                        publisher as Publisher, 
                        bookTitulo as BibliographyType
                    FROM Referencia
                    WHERE situacao = 'Aprovada'
             """

    db.gerarCSV("JABREF", strSQL)


if __name__ == '__main__':
    main()
