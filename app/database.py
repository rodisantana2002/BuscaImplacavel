import sys
import sqlite3
import os
import logging
from sqlite3 import Error

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

class database(object):
    def __init__(self):
        self.pathOrigem = '../bases/database/bot.db'

    def _getConn(self):
        try:
            conn = sqlite3.connect(self.pathOrigem)
            return conn
        except Error as e:
            logger.debug(e)
            return None
        return sqlite3.connect(self.pathOrigem)

    def _criarTabela(self, strSQL):
        cn = self._getConn()
        
        try:
            cursor = cn.cursor()
            cursor.execute(strSQL)
            logger.debug("tabela criada com sucesso")
        except Error as e:
            logger.debug(e)
        cn.close()

    def _gerarTabelas(self):
        tabelas = []
        tabelas.append("""CREATE TABLE Pesquisa (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                descricao VARCHAR(30), 
                                                situacao VARCHAR(20),
                                                criado_em VARCHAR(12));""")

        tabelas.append("""CREATE TABLE Artigo (id VARCHAR(50) NOT NULL PRIMARY KEY , 
                                               situacao VARCHAR(20),
                                               titulo TEXT, 
                                               ano VARCHAR(4), 
                                               autores TEXT, 
                                               resumo TEXT, 
                                               keywords TEXT, 
                                               doi TEXT, 
                                               url TEXT, 
                                               tipo_publicacao VARCHAR(30), 
                                               base_origem VARCHAR(20), 
                                               pesquisa_id INTEGER,
                                               criado_em VARCHAR(12));""")

        tabelas.append("""CREATE TABLE ArtigoElemento (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                       situacao VARCHAR(20),
                                                       txtorigem TEXT, 
                                                       txttranslate TEXT, 
                                                       tipo VARCHAR(3), 
                                                       artigo_id VARCHAR(50),
                                                       criado_em VARCHAR(12));""")

        tabelas.append("""CREATE TABLE Referencia (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                       identificador VARCHAR(10), 
                                                       descricao TEXT, 
                                                       artigo_id VARCHAR(50),
                                                       criado_em VARCHAR(12))""")

        for tabela in tabelas:
            self._criarTabela(tabela)

def main():
    db = database()
    db._gerarTabelas()


if __name__ == '__main__':
    main()
