'''
Mesclador de arquivos PDF
'''
import PyPDF2
import os

#usa a função PdfMerger() para mesclar os arquivos.
merger = PyPDF2.PdfMerger()

#faz uma lista com os arquivos a mesclar
lista_arquivos = os.listdir('Arquivos_Estudos/automacao_pdf_hashtag')
##ordena a lista
lista_arquivos.sort()
#roda cada arquivo da lista e primeiro verifica se a extensão é pdf, 
# se for adiciona a function merger
for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'Arquivos_Estudos/automacao_pdf_hashtag/{arquivo}')

# salva o arquivo onde quisermos
merger.write('Arquivos_Estudos/automacao_pdf_hashtag/PDF FINAL.pdf')