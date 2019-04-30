# -*- coding: utf-8 -*-

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal,LTTextBoxHorizontal, LTChar, LTRect, LTLine, LTAnon
from io import StringIO

fp = open("../files/arquivo2.pdf", 'rb')
def lerPDF(arquivoPDF):
    # PDFResourceManager Usado para armazenar recursos compartilhados
    # como fontes e imagens
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams(line_margin=1, word_margin=0.3, char_margin=100,
                            line_overlap=0.1, boxes_flow=0.1)
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
    process_pdf(recursos, dispositivo, arquivoPDF, check_extractable=True)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

with open('convertedFile.txt', "wb") as txt_file:
    txt_file.write(lerPDF(fp).encode("utf-8"))

fp.close()

fp = open("convertedFile.txt", 'rb')
for linha in fp:    
    x = str(linha)
    # y = x.replace('\f', "*****")
    # z = y.replace('\n', "\$$" )    

    print(x)    

    # if "\xe2" in z:
    #     print(repr(z)

    # if x.startswith("\x0c"):
    #     y = x.replace('\x0c', "*****")
    # elif x.startswith("\n"):        
    #     y = x.replace('\n', "%%")
    # elif x.startswith(' \n'):
    #     y = x.replace(' \n', "%%")
    # elif x.endswith('\n'):   
    #     y = x.replace('\n', "$$" )

    # print(y)        
# fp.close()    


# var = '\x0c Abstract. Background – Startup companies are becoming important suppliers'
# x= var.replace('\x0c', '\n |')
# print(x)




















# parser = PDFParser(fp)
# doc = PDFDocument()
# parser.set_document(doc)
# doc.set_parser(parser)
# doc.initialize('')
# rsrcmgr = PDFResourceManager()
# laparams = LAParams()
# laparams.char_margin = 1.0
# laparams.word_margin = 1.0
# device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# extracted_text = ''

# for page in doc.get_pages():
#         interpreter.process_page(page)
#         layout = device.get_result()
#         for lt_obj in layout:
#             if isinstance(lt_obj, LTTextBox):  # isinstance(lt_obj, LTTextLine)
#                 extracted_text += lt_obj.get_text()

# with open('convertedFile.txt', "wb") as txt_file:
#     txt_file.write(extracted_text.encode("utf-8"))


# import PyPDF2
# import os
# """Lê documento PDF e retorna texto extraido"""

# # esta função recebe o caminho do arquivo pdf e retorna seu texto extraido num string


# def getPDFContent(path):
#     content = ""

#     # abre o arquivo pdf e cria um objeto reader
#     f = open(path, "rb")
#     pdf = PyPDF2.PdfFileReader(f)       # objeto que representa o documento

#     # Itera pelas páginas do documento
#     for i in range(0, pdf.getNumPages()):
#         # Extrai texto da pagina e apenda no string content
#         content += pdf.getPage(i).extractText() 

#     # fecha o arquivo
#     f.close()
#     return content


# # programa principal, executado ao ativar o módulo
# print('Extrai texto de arquivo PDF.')
# print(os.getcwd())
# print(os.listdir())
# print('----------------------------')
# print('Entre nome ou caminho de arquivo PDF:')

# arq = input()
# if not arq.endswith('.pdf'):
#     arq = arq + '.pdf'

# stx = getPDFContent(arq)

# # txt = stx.split('\n')

# print('Texto extraido (primeiros 100 caracteres):')
# print('-------------------------------------------')
# print()
# # for str in stx:
# print(stx)    
# print()
# print('-------------------------------------------')    
