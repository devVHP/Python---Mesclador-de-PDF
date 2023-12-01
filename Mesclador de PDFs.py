import PyPDF2
import os

merger = PyPDF2.PdfMerger()
listaArquivos = os.listdir('arquivos')
listaArquivos.sort()

for arquivos in listaArquivos:
    if '.pdf' in arquivos:
        merger.append(f'arquivos/{arquivos}')

merger.write('PDF FINAL.pdf')