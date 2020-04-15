import sys
import os
import logging
import model.models as modelo
import bibtexparser

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)

pathOrigem = '../bases/referencias/'

class Fluxo(object):
    
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
    
    def _carregarReferencias(self, pesquisa_id):
        # Passo 01 carregar dos dados para os arquivos bibtext
        arquivos = self._obterArquivos(pathOrigem, "bibtext")
        refs=[]        
        if len(arquivos) > 0:            
            for arq in arquivos:                                                
                with open(arq) as bibtex_file:
                    bib_database = bibtexparser.load(bibtex_file)
                    for ref in bib_database.entries:
                        # popula valores no objeto
                        referencia = modelo.Referencia()
                        if 'doi' in ref:
                            referencia.doi = ref['doi']
                        else:
                            referencia.doi = ""

                        if 'url' in ref:
                            referencia.url = ref['url']
                        else:
                            referencia.url = ""

                        if 'title' in ref:
                            referencia.titulo = ref['title']
                        else:
                            referencia.titulo = ""

                        if 'year' in ref:
                            referencia.ano = ref['year']
                        else:
                            referencia.ano = ""

                        if 'publisher' in ref:
                            referencia.publisher = ref['publisher']
                        else:
                            referencia.publisher = ""
                                
                        if 'booktitle' in ref:
                            referencia.bookTitulo = ref['booktitle']
                        else:
                            referencia.bookTitulo = ""
                            
                        if 'author' in ref:
                            referencia.autores = ref['author']
                        else:
                            referencia.autores = ""
                            
                        # demais valores
                        referencia.pesquisa_id = pesquisa_id
                        referencia.resumo = ""
                        referencia.keywords = ""
                        referencia.texto_rtf = ""
                        referencia.referencia = ""                                
                        referencia.arquivo_origem = os.path.basename(arq)
                        refs.append(referencia)                        
                        referencia.add(referencia)
                
        else:
            logger.debug('---> Não foram encontrados arquivos BibText para serem lidos')
        
        return refs

def main():
    # # pesquisa base nivel 0
    # pesquisa = modelo.Pesquisa()
    # pesquisa.descricao="Mapeamentos e SRL"
    # pesquisa.objetivo="Pesquisa sobre SaaS - com referencias sobre mapeamentos e srl sobre saas"
    # pesquisa.add(pesquisa)
    # # snowball nivel 1
    # pesquisa = modelo.Pesquisa()
    # pesquisa.descricao="Pesquisa Artigos Primários "
    # pesquisa.objetivo="Snow-Ball nível 1"
    # pesquisa.add(pesquisa)
    
    flx = Fluxo()
    for ref in flx._carregarReferencias(3):
        print(ref.__str__())
        print("\n")

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
    
    
    
if __name__ == '__main__':
    main()        
