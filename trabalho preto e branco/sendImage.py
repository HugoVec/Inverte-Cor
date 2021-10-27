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
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

#variaveis
top = tk.Tk(className='Projeto - Limiarização')

#define tamanho da pagina
top.geometry("500x200")

#função que pega imagem
def enviaImagem():
    #path = filedialog.askopenfilename()
    dirImage = filedialog.askopenfile(mode='r',filetypes =[('JPG', '*.jpg'),('PNG', '*.png'),('TIFF', '*.tiff')])
    #dirImage = filedialog.askopenfilename()
    image = os.path.basename(dirImage.name)

    if len(image) > 0:
        local=dirImage.name
        #caminho salvar imagem
        destination=r'trabalho preto e branco/imagens/'+image
        shutil.copyfile(local, destination)
        
        img = cv2.imread(destination, 0)

        ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        images = [img, 0, th1, img, 0, th2, blur, 0, th3]
        
        titles = ['Imagem original com ruído', 'Histograma', 'Limiar Global (v = 127)',
                'Imagem original com ruído', 'Histograma', "Limiar de Otsu",
                'Imagem filtrada gaussiana', 'Histograma', "Limiar de Otsu"]
        
        mpl.backend_bases.NavigationToolbar2.toolitems = (
            ('Save', 'Salvar imagem', 'filesave', 'save_figure'),
        )

        for i in range(3):
            plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
            plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
            plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
            plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
        plt.show()
        
    else:
        print('Erro')

#label informativo
description = tk.Label(top, text='Tipos de imagem permitidos jpg, png ou tiff', relief=FLAT)

#botao enviar dados
button = tk.Button(top, text ="Enviar", command = enviaImagem)

description.pack()
button.pack()
top.mainloop()