#imports
import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import shutil

#variaveis
top = tk.Tk(className='Projeto - Limiarização')

#define tamanho da pagina
top.geometry("300x200")

#função que pega imagem
def enviaImagem():
    #tipos de arquivos permitidos
    dirImage = filedialog.askopenfile(mode='r',filetypes =[('JPG', '*.jpg'),('PNG', '*.png'),('TIFF', '*.tiff')])

    #caminho imagem selecionada
    image = os.path.basename(dirImage.name)

    #verifica se é um arquivo valido
    if len(image) > 0:

        #nome da aplicação
        local=dirImage.name
        
        #caminho salvar imagem
        destination=r'trabalho preto e branco/imagens/'+image

        #copia o documento para pasta do projeto
        shutil.copyfile(local, destination)

        #dados da imagem
        image = cv2.imread(local, 0)

        #dados da imagem a partid do caminho
        img = cv2.imread(destination, 0)
        
        #fecha o tinker que requere a imagem
        _quit()

        #blur tira ruidos da imagem
        blur = cv2.GaussianBlur(img, (5, 5), 0)

        #retorno da imagem cinza
        retorno3, imagemCinza = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        #botão salvar da aplicação plt
        mpl.backend_bases.NavigationToolbar2.toolitems = (
            ('Save', 'Salvar imagem', 'filesave', 'save_figure'),
        )
        
        #titulo da aplicação plt
        plt.figure('Projeto - Limiarização')

        #imagem cinza
        plt.subplot(3, 2, 0 * 3 + 1), plt.imshow(img, 'gray')
        plt.title('Imagem cinza'), plt.xticks([]), plt.yticks([])
        
        #histograma
        plt.subplot(2, 2, 0 * 3 + 2), plt.hist(img.ravel(), 256,[0,256])
        plt.title('Histograma'), plt.xticks([]), plt.yticks([])

        #imagem binarizada
        plt.subplot(3, 2, 0 * 3 + 3), plt.imshow(imagemCinza, 'gray')
        plt.title('Imagem Binarizada'), plt.xticks([]), plt.yticks([])
        
        #mostra as imagens
        plt.show()

    else:
        #mensagem de erro no console
        print('Erro')

#função fechar a aplicação
def _quit():
    top.quit()
    top.destroy() 

#botão sair                    
quit = tk.Button(master=top, text="Sair", command=_quit, height=1, width=30,  bg='#DC143C', fg='white')


#label informativo
description = tk.Label(top, text='Tipos de imagem permitidos jpg, png ou tiff', relief=FLAT)

#botao enviar dados
button = tk.Button(top, text ="Enviar", command = enviaImagem, height=1, width=30,   bg='#006400', fg='white')

#apresentação tinker
quit.pack(side=tk.BOTTOM)
description.pack()
button.pack()
top.mainloop()
