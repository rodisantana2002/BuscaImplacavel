import sys
import sqlite3
import os
import logging
import csv

from sqlite3 import Error

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

class database(object):
    def __init__(self):
        # self.pathOrigem = '../bases/database/bot.db'
        self.pathOrigem = '../BuscaImplacavel/bases/database/bot.db'

    def _getConn(self):
        try:
            conn = sqlite3.connect(self.pathOrigem)
            return conn
        except Error as e:
            logger.debug(e)
            return None

    def _criarTabela(self, strSQL):             
        try:
            cn = self._getConn()                    
            cursor = cn.cursor()
            cursor.execute(strSQL)
            logger.debug("tabela criada com sucesso")
        except Error as e:
            logger.debug(e)
        cn.close()

    def _gerarTabelas(self):
        tabelas = []
        tabelas.append("""CREATE TABLE Pesquisa (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                situacao VARCHAR(20),
                                                descricao VARCHAR(30), 
                                                objetivo TEXT,
                                                criado_em VARCHAR(20));""")

        tabelas.append("""CREATE TABLE Referencia (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                situacao VARCHAR(20),
                                                titulo TEXT, 
                                                ano VARCHAR(4), 
                                                autores TEXT, 
                                                resumo TEXT, 
                                                keywords TEXT, 
                                                doi TEXT, 
                                                url TEXT, 
                                                publisher TEXT,
                                                bookTitulo TEXT, 
                                                arquivo_origem VARCHAR(20), 
                                                pesquisa_id INTEGER,
                                                texto_rtf TEXT,
                                                criado_em VARCHAR(20));""")

        tabelas.append("""CREATE TABLE ReferenciaElemento (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                                       situacao VARCHAR(20),
                                                       tipo VARCHAR(10),
                                                       linha_pos INTEGER,
                                                       txt_origem TEXT, 
                                                       txt_translate TEXT, 
                                                       referencia_id VARCHAR(50),
                                                       criado_em VARCHAR(12));""")

        for tabela in tabelas:
            self._criarTabela(tabela)

    def salvarArtigo(self):
        cn = self._getConn()

        # string busca
        strSQL_BUSCAR = """SELECT id FROM Artigo WHERE id = ?"""

        # string insert
        strSQL_INSERT = """INSERT INTO Artigo (id,situacao,titulo,ano,autores,resumo,keywords,doi,url,tipo_publicacao,base_origem,pesquisa_id,criado_em)  
                           VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"""       

        # string de atualização da situação
        strSQL_UPDATE = """ UPDATE Artigo SET situacao = ? WHERE id = ?"""    

        try:
            cursor_reader = cn.cursor()
            with open(self.pathConvertido, 'r') as arq:
                reader = csv.DictReader(arq)
                cursor_reader = cn.cursor()
                for row in reader:                        
                        cursor_reader.execute(strSQL_BUSCAR, (row['id'],))
                        if cursor_reader.fetchall().__len__() == 0:
                            cursor_exec = cn.cursor()
                            artigo = [(row['id'], 
                                       row['situacao'],
                                       row['title'], 
                                       row['year'], 
                                       row['author'], 
                                       '', 
                                       row['keywords'], 
                                       row['doi'], 
                                       row['url'], 
                                       row['tipo'], 
                                       row['base'], 
                                       '', 
                                       '')]

                            cursor_exec.executemany(strSQL_INSERT, artigo)
                            cn.commit()
                            logger.debug("Artigos inseridos com sucesso")
                        else:
                            cursor_exec = cn.cursor()
                            artigo = (row['situacao'], row['id'],)

                            cursor_exec.execute(strSQL_UPDATE, artigo)
                            cn.commit()
                            logger.debug("Artigos atualizados com sucesso")
        except Error as e:
            cn.rollback()
            logger.debug(e)
        cn.close()
                    

    def salvarArtigoElemento(self):
        pass    

    def salvarReferencias(self):
        pass    

    def _obterArquivos(self, path, tipo):
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith("." + tipo)])

def main():
    db = database()
    db._gerarTabelas()
    # db.salvarArtigo()


if __name__ == '__main__':
    main()
