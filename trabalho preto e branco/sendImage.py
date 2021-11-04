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
        
        #calculo treshold
        numero = 256

        #Histograma
        histograma, bordas = np.histogram(image, bins=numero)

        #Media das bordas
        media = (bordas[:-1] + bordas[1:]) / 2.
        
        #Peso histograma
        pesoHist1 = np.cumsum(histograma)
        pesoHist2 = np.cumsum(histograma[::-1])[::-1]
        
        #Variancia
        mediaVar1 = np.cumsum(histograma * media) / pesoHist1
        mediaVar2 = (np.cumsum((histograma * media)[::-1]) / pesoHist2[::-1])[::-1]
        variancia = pesoHist1[:-1] * pesoHist2[1:] * (mediaVar1[:-1] - mediaVar2[1:]) ** 2
        
        #Valor maximo
        valorMaximo = np.argmax(variancia)
        
        #resultado do limiar
        limiar = media[:-1][valorMaximo]

        #dados da imagem a partid do caminho
        img = cv2.imread(destination, 0)
        
        #fecha o tinker que requere a imagem
        _quit()

        #retorno da imagem binarizada
        retorno1, imagemBinaria = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY_INV)
        
        #retorno do histograma
        retorno2, histograma = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY_INV)

        #blur tira ruidos da imagem
        blur = cv2.GaussianBlur(img, (5, 5), 0)

        #retorno da imagem cinza
        retorno3, imagemCinza = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        #array com os dados das imagens
        images = [img, 0, imagemBinaria, img, 0, histograma, blur, 0, imagemCinza]
        
        #botão salvar da aplicação plt
        mpl.backend_bases.NavigationToolbar2.toolitems = (
            ('Save', 'Salvar imagem', 'filesave', 'save_figure'),
        )
        
        #titulo da aplicação plt
        plt.figure('Projeto - Limiarização')

        #Apresentação

        #imagem cinza
        plt.subplot(3, 2, 0 * 3 + 1), plt.imshow(images[0 * 3], 'gray')
        plt.title('Imagem cinza'), plt.xticks([]), plt.yticks([])
        
        #histograma
        plt.subplot(2, 2, 0 * 3 + 2), plt.hist(images[0 * 3].ravel(), 256,[0,256])
        plt.title('Histograma'), plt.xticks([]), plt.yticks([])

        #imagem binarizada
        plt.subplot(3, 2, 0 * 3 + 3), plt.imshow(images[0 * 3 + 2], 'gray')
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
