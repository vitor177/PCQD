import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def total_xplot2c(variavel1, variavel2, data, num_figura, titulo, diafinal, mes, ano, lim_sy, lim_iy, und_y, tam_font, var1, var2, nome_arquivo):
    
    # Títulos para as subplots
    titulo01 = f"{titulo} ({mes} 01 to 10, {ano})"
    titulo02 = f"{titulo} ({mes} 11 to 20, {ano})"
    titulo03 = f"{titulo} ({mes} 21 to {diafinal}, {ano})"

    # Definindo as cores
    cor1 = 'red'
    cor2 = [0.12, 0.64, 0.82]

    # Transformando o formato da data para datetime
    data = pd.to_datetime(data, format='%d/%m/%Y %H:%M:%S')

    # Dividindo os dados em três partes
    datap1 = data.iloc[:14400]
    datap2 = data.iloc[14401:28800]
    datap3 = data.iloc[28801:]

    variavelp1 = variavel1.iloc[:14400]
    variavelp2 = variavel1.iloc[14401:28800]
    variavelp3 = variavel1.iloc[28801:]

    variavel2p1 = variavel2.iloc[:14400]
    variavel2p2 = variavel2.iloc[14401:28800]
    variavel2p3 = variavel2.iloc[28801:]

    # Criando a figura
    plt.figure(num_figura, figsize=(12, 6))
    
    # Primeira subplot
    plt.subplot(3, 1, 1)
    plt.plot(datap1, variavelp1, color=cor1)
    plt.plot(datap1, variavel2p1, color=cor2)
    plt.grid(True, which='minor')
    plt.ylim([lim_iy, lim_sy])
    plt.ylabel(und_y)
    plt.title(titulo01)
    plt.legend([var1, var2], loc='upper right', ncol=2, frameon=False)
    plt.xticks(rotation=45)
    
    # Segunda subplot
    plt.subplot(3, 1, 2)
    plt.plot(datap2, variavelp2, color=cor1)
    plt.plot(datap2, variavel2p2, color=cor2)
    plt.grid(True, which='minor')
    plt.ylim([lim_iy, lim_sy])
    plt.ylabel(und_y)
    plt.title(titulo02)
    plt.legend([var1, var2], loc='upper right', ncol=2, frameon=False)
    plt.xticks(rotation=45)
    
    # Terceira subplot
    plt.subplot(3, 1, 3)
    plt.plot(datap3, variavelp3, color=cor1)
    plt.plot(datap3, variavel2p3, color=cor2)
    plt.grid(True, which='minor')
    plt.ylim([lim_iy, lim_sy])
    plt.ylabel(und_y)
    plt.title(titulo03)
    plt.legend([var1, var2], loc='upper right', ncol=2, frameon=False)
    plt.xticks(rotation=45)
    
    # Salvando os gráficos como PDF e PNG
    plt.savefig(f"{nome_arquivo}_{titulo}_comp2.pdf", format='pdf')
    plt.savefig(f"{nome_arquivo}_{titulo}_comp2.png", format='png')
    #plt.show()

