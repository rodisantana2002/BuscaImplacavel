import sys
import os
import logging
import model.models as modelo

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

pathDestino = '../bases/referencias/'

class fluxo(object):
    
    def __init__(self):
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/fluxo.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)
    
    def importarBIBFile(self):
        pass

    def _obterArquivos(self, path, tipo):
        return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith("." + tipo)])


def main():
    # pesquisa base nivel 0
    pesquisa = Pesquisa()
    pesquisa.descricao="Mapeamentos e SRL"
    pesquisa.objetivo="Pesquisa sobre SaaS - com referencias sobre mapeamentos e srl sobre saas"
    pesquisa.add(pesquisa)
    # snowball nivel 1
    pesquisa = Pesquisa()
    pesquisa.descricao="Mapeamentos e SRL"
    pesquisa.objetivo="Pesquisa sobre SaaS - com referencias sobre mapeamentos e srl sobre saas"
    pesquisa.add(pesquisa)


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
