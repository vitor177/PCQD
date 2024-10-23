import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def total_xplot(variavel, data, num_figura, titulo, dia_final, mes, ano, lim_sy, lim_iy, und_y, tam_font, cor, nome_arquivo):
    titulo01 = f"{titulo} ({mes} 01 to 10, {ano})"
    titulo02 = f"{titulo} ({mes} 11 to 20, {ano})"
    titulo03 = f"{titulo} ({mes} 21 to {dia_final}, {ano})"

    # Transformando o formato da data
    data = pd.to_datetime(data, format='%d/%m/%Y %H:%M:%S')

    datap1 = data[:14400]
    datap2 = data[14400:28800]
    datap3 = data[28800:]

    variavelp1 = variavel[:14400]
    variavelp2 = variavel[14400:28800]
    variavelp3 = variavel[28800:]

    plt.figure(num_figura, figsize=(12, 6))  # Define o tamanho da figura

    # Subplot 1
    plt.subplot(3, 1, 1)
    plt.plot(datap1, variavelp1, color=cor)
    plt.title(titulo01)
    plt.ylabel(und_y)
    plt.ylim(lim_iy, lim_sy)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=tam_font)
    plt.yticks(fontsize=tam_font)

    # Subplot 2
    plt.subplot(3, 1, 2)
    plt.plot(datap2, variavelp2, color=cor)
    plt.title(titulo02)
    plt.ylabel(und_y)
    plt.ylim(lim_iy, lim_sy)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=tam_font)
    plt.yticks(fontsize=tam_font)

    # Subplot 3
    plt.subplot(3, 1, 3)
    plt.plot(datap3, variavelp3, color=cor)
    plt.title(titulo03)
    plt.ylabel(und_y)
    plt.ylim(lim_iy, lim_sy)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(fontsize=tam_font)
    plt.yticks(fontsize=tam_font)

    # Ajustar o layout
    plt.tight_layout()

    # Salvar a figura em PDF e PNG
    plt.savefig(f"{nome_arquivo}_{titulo}x.pdf", format='pdf', bbox_inches='tight')
    plt.savefig(f"{nome_arquivo}_{titulo}x.png", format='png', bbox_inches='tight')

    #plt.show()