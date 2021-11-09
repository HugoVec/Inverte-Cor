import csv
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

#variaveis
top = tk.Tk(className='Projeto - Sistema Linear')

#define tamanho da pagina
top.geometry("300x200")

#função que pega imagem
def enviaImagem():
    #tipos de arquivos permitidos
    arquivo = filedialog.askopenfile(mode='r',filetypes =[('CSV', '*.csv')])

    arquivoLocal = arquivo.name

    arquivo = open(arquivoLocal)
    reader = csv.reader(arquivo, delimiter=',')
    c = len(next(reader))

    l = sum(1 for itens in reader)
    l = l
    
  
    #print(reader)
    #print(c)
    #print(l)

    valor=np.loadtxt(arquivoLocal,
                        delimiter=',',
                        unpack=True,
                        dtype='str')


    linhas = csv.reader(arquivo)

    for linha in linhas:
        print(linha)

    i=0
    x=0
    b = []
    a = []
    while i < c:
        while x < l:
            if(i + 1 == c):
                
                b.append(int(valor[i][x]))
                #print('caralho:',valor[i][x])
            else:
                a.append(int(valor[i][x]))
                print(valor[i][x])
            x=x+1
        x=0
        i=i+1
    print(b)
    print(a)

#função fechar a aplicação
def _quit():
    top.quit()
    top.destroy() 

#botão sair                    
quit = tk.Button(master=top, text="Sair", command=_quit, height=1, width=30,  bg='#DC143C', fg='white')


#label informativo
description = tk.Label(top, text='', relief=FLAT)

#botao enviar dados
button = tk.Button(top, text ="Enviar", command = enviaImagem, height=1, width=30,   bg='#006400', fg='white')

#apresentação tinker
quit.pack(side=tk.BOTTOM)
description.pack()
button.pack()
top.mainloop()