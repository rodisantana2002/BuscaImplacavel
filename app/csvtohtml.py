
import re
import sys
import os
import logging
import csv

from datetime import datetime

# log config
logging.basicConfig()
logger = logging.getLogger('Log.')
logger.setLevel(logging.DEBUG)
pathOrigem = '../files/traduzidos/'
pathDestino = '../files/processados/'

class csvtohtml(object):
    def __init__(self):
        self.homeDir = "../logs"
        self.logFile = self.homeDir + '/csvtohtml.log'
        self.logger_handler = logging.FileHandler(self.logFile, mode='w')
        self.logger_handler.setLevel(logging.DEBUG)
        # Associe o Handler ao  Logger
        logger.addHandler(self.logger_handler)

    def _converterCSVtoHTML(self, arquivoCSV):
        try:
            html_file = "%s.html" % os.path.basename(arquivoCSV)[0:-4]
            csv_file = "%s.csv" % os.path.basename(arquivoCSV)[0:-4]

            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

            html = ''.join(self._criarHTML(csv_file))

            with open(pathDestino + html_file, "w") as arq:
                arq.write(str(html))

            return '---> {} ---[ ok ] Arquivo processado com sucesso [{}]'.format(data_atual, os.path.basename(arquivoCSV))
        except:
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Arquivo não pode ser convertido'.format(data_atual)

    def _criarHTML(self, arquivo):
        strHTML = []
        strHTML.append("<html>\n")
        strHTML.append("<head>\n")
        strHTML.append("<meta charset='UTF-8'>\n")
        strHTML.append("<link rel = 'stylesheet' href = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity = 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin = 'anonymous'>")
        strHTML.append("")
        strHTML.append("</head>\n")

        strHTML.append("")
        strHTML.append("<Body>\n")
        strHTML.append("<h2 align = 'center' > {} </h2 >\n".format(os.path.basename(arquivo)[0:-4]))

        strHTML.append("<table class='table table-striped'> \n")
        strHTML.append("</br>")

        with open(pathOrigem + arquivo, 'r') as arq:
            reader = csv.DictReader(arq)
            id = 1

            for row in reader:                
                if len(row['txtorigem']) > 0:  # não eh uma linha em branco
                    if len(row['txttranslate'])==0:
                        strHTML.append("<tr align = 'left'><td>{} ".format(row['txtorigem']))
                    else:    
                        strHTML.append("<tr align = 'left'><td>{} ".format(row['txttranslate']))

                        if row['tipo'] != 'REF':
                            strHTML.append("<button type='button' class='btn btn-link btn-sm' data-toggle='collapse' href='#collapseOriginal{}' role='button' aria-expanded='false' aria-controls='collapseOriginal'>".format(id))
                            strHTML.append("<< ver original >>")
                            strHTML.append("</button>")

                            strHTML.append("<div class='collapse' id='collapseOriginal{}'>".format(id))
                            strHTML.append(
                                "<div class = 'text-info'> {}".format(row['txtorigem']))
                            strHTML.append("</div>")
                            strHTML.append("</div>")
                            strHTML.append("</tr></td>")

                            id+=1

        strHTML.append("</table>\n")

        strHTML.append("<script src = 'https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity = 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin = 'anonymous' > </script >")
        strHTML.append("<script src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js' integrity = 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin = 'anonymous' > </script >")
        strHTML.append("<script src = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity = 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin = 'anonymous' > </script >")      
        strHTML.append("</Body>\n")
        strHTML.append("</html>\n")
        
        return strHTML
    
    def _popularIndice(self):
        
        strHTML = []
        strHTML.append("<html>\n")
        strHTML.append("<head>\n")
        strHTML.append("<meta charset='UTF-8'>\n")
        strHTML.append("<link rel = 'stylesheet' href = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity = 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin = 'anonymous'>")
        strHTML.append("")
        strHTML.append("</head>\n")

        strHTML.append("")
        strHTML.append("<Body>\n")

        arquivos = self._obterArquivos(pathOrigem, "csv")
        if len(arquivos) > 0:
            for arquivo in arquivos:
                html_file = "%s.html" % os.path.basename(arquivo)[0:-4]

                # with open(arquivo, 'r') as arq:
                #     reader = csv.DictReader(arq)
                #     id = 1


                #     strHTML.append("</br>")
                #     for row in reader:
                #         if len(row['txtorigem']) > 0:  # não eh uma linha em branco
                #             strHTML.append("<div class='col-12'")
                #             strHTML.append("<div class='card'>")
                #             strHTML.append("<h5 class='card-header'>{}</h5>".format(row['arquivo']))
                #             strHTML.append("<div class='card-body'>")
                #             if row['tipo'] == 'TIT':
                #                 strHTML.append("<h4 class='card-title'>{}</h4>".format(row['txttranslate']))
                #             else:
                #                 strHTML.append("<h4 class='card-title'>Título não identificado</h4>")

                #             if row['tipo'] == 'ABS':
                #                 strHTML.append("<p class='card-text'>{}</p>".format(row['txttranslate']))
                #             else:
                #                 strHTML.append("<p class='card-text'>...</p>")
                            
                #             strHTML.append("<a href='#{}' class='btn btn-primary'>Visializar</a>".format(pathDestino + html_file))
                #             strHTML.append("</div>")                    
                #             strHTML.append("</div>")
                #             strHTML.append("</div>")

                #             id += 1

                #     strHTML.append("</br>")

        strHTML.append("<script src = 'https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity = 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin = 'anonymous' > </script >")
        strHTML.append("<script src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js' integrity = 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin = 'anonymous' > </script >")
        strHTML.append("<script src = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity = 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin = 'anonymous' > </script >")
        strHTML.append("</Body>\n")
        strHTML.append("</html>\n")

        return strHTML            


    def _gerarIndice(self):
        try:
            indice_file = "index.html"

            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

            html = ''.join(self._popularIndice())

            with open(pathDestino + indice_file, "w") as arq:
                arq.write(str(html))

            return '---> {} ---[ ok ] Indice gerado com sucesso'.format(data_atual)

        except Exception as exc:
            print(exc)
            data_hora_atuais = datetime.now()
            data_atual = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            return '---> {} ---[erro] Indice não pode ser gerado'.format(data_atual)

    def gerarHTML(self):
        logger.debug('----------------------------------------------------------------------------------------------')
        logger.debug('---> Iniciando geração dos arquivos HTMLs')
        logger.debug('----------------------------------------------------------------------------------------------')

        # Passo 01 ler arquivos csv e processar a geração dos HTMLs
        arquivos = self._obterArquivos(pathOrigem, "csv")
        if len(arquivos) > 0:
            for arq in arquivos:
                logger.debug(self._converterCSVtoHTML(arq))
            logger.debug(self._gerarIndice())
            logger.debug('----------------------------------------------------------------------------------------------')

        else:
            logger.debug(
                '---> Não foram encontrados arquivos CSV para serem processados')

    def _obterArquivos(self, path, tipo):
            return ([path+file for p, _, files in os.walk(os.path.abspath(path)) for file in files if file.lower().endswith("." + tipo)])

def main():
    conv = csvtohtml()
    conv.gerarHTML()

if __name__ == '__main__':
    main()
