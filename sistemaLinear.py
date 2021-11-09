#Feito por: 
#Rafael Bassan D9614F1

import csv
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import numpy as np
import pandas as pd
import re

#variaveis
top = tk.Tk(className='Projeto - Sistema Linear')

#define tamanho da pagina
top.geometry("300x200")

#função que pega imagem
def contagem():
    #tipos de arquivos permitidos
    arquivo = filedialog.askopenfile(mode='r',filetypes =[('CSV', '*.csv')])

    arquivoLocal = arquivo.name

    arquivo = open(arquivoLocal)
    reader = csv.reader(arquivo, delimiter=',')
    c = len(next(reader))

    l = sum(1 for itens in reader)
    l = l + 1
    
  
    #print(reader)
    #print(c)
    #print(l)

    valor=np.loadtxt(arquivoLocal,
                        delimiter=',',
                        unpack=True,
                        dtype='str')
    i=0
    x=0

    b = []
    a = []
    v = []
    
    while i < l:
        while x < c:
            if(x + 1 == c):
                u = valor[x][i]
                u = re.sub('[^0-9-]', '', u)  
                b.append(int(u))
            else:
                u = valor[x][i]
                u = re.sub('[^0-9-]', '', u)             
                a.append(int(u))
                
            if(x + 1 == c):
                v.append(a) 

            x=x+1
        
        a = [] 
        x=0
        i=i+1 
  
    conta = np.linalg.solve(v, b)
    texto = "Resultado: " + str(conta)

    description = tk.Label(top, text=texto, relief=FLAT)
    description.pack()
    
    #print(conta)
    #label informativo

#função fechar a aplicação
def _quit():
    top.quit()
    top.destroy() 

#botão sair                    
quit = tk.Button(master=top, text="Sair", command=_quit, height=1, width=30,  bg='#DC143C', fg='white')

description = tk.Label(top, text='', relief=FLAT)



#botao enviar dados
button = tk.Button(top, text ="Enviar", command = contagem, height=1, width=30,   bg='#006400', fg='white')
description.pack()
#apresentação tinker
quit.pack(side=tk.BOTTOM)

button.pack()
top.mainloop()