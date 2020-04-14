import sys
import os
import logging
import model.models as modelo

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)


class fluxo(object):
    
    def __init__(self):
        pass
    
    def importarBIBFile():
        pass
        

def main():
    pass
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

    # linha = Translate() 
    # linha.linha_pos = 1
    # linha.tipo ="ABS"
    # linha.txt_origem = "origem"
    # linha.txt_translate = "translate"
    # linha.referencia_id = 1
    # linha.add(linha)
      
    
if __name__ == '__main__':
    main()        