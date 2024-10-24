import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import pandas as pd

def total_eplot(variavel1, variavel2, variavel3, num_figura, titulo, titulo1, titulo2, titulo3, nome_arquivo):
    variavel1 = pd.DataFrame(variavel1)
    variavel2 = pd.DataFrame(variavel2) if variavel2 is not None else pd.DataFrame()
    variavel3 = pd.DataFrame(variavel3) if variavel3 is not None else pd.DataFrame()
    
    cor1 = 'red'
    cor2 = [0.12, 0.64, 0.82]
    cor3 = [1, 0.75, 0.035]
    faixa = np.arange(0, 1850, 50)
    faixa1 = np.arange(0, 1900, 100)
    faixa_new = np.arange(0, 1805, 5)

    porcentagem1 = np.array(variavel1.iloc[:, 3], dtype=float)
    suave1 = splev(faixa_new, splrep(faixa, porcentagem1))

    if not variavel2.empty and variavel3.empty:
        porcentagem2 = np.array(variavel2.iloc[:, 3], dtype=float)
        suave2 = splev(faixa_new, splrep(faixa, porcentagem2))

    if not variavel2.empty and not variavel3.empty:
        porcentagem2 = np.array(variavel2.iloc[:, 3], dtype=float)
        porcentagem3 = np.array(variavel3.iloc[:, 3], dtype=float)
        suave2 = splev(faixa_new, splrep(faixa, porcentagem2))
        suave3 = splev(faixa_new, splrep(faixa, porcentagem3))

    plt.figure(num_figura, figsize=(9.5, 4))
    
    if variavel2.empty and variavel3.empty:
        plt.plot(faixa_new, suave1, color=cor1, label=titulo1)
        plt.legend(loc='upper right')
    
    if not variavel2.empty and variavel3.empty:
        plt.plot(faixa_new, suave1, color=cor1, label=titulo1)
        plt.plot(faixa_new, suave2, color=cor2, label=titulo2)
        plt.legend(loc='upper right')
    
    if not variavel2.empty and not variavel3.empty:
        plt.plot(faixa_new, suave1, color=cor1, label=titulo1)
        plt.plot(faixa_new, suave2, color=cor2, label=titulo2)
        plt.plot(faixa_new, suave3, color=cor3, label=titulo3)
        plt.legend(loc='upper right')

    plt.grid(True)
    plt.ylim([0, 20])
    plt.ylabel('Fração de Energia [%]')
    plt.xlabel('Irradiância [W/m²]')
    plt.xticks(faixa1, [str(i) for i in faixa1])
    plt.xlim([0, 1800])
    plt.savefig(f"{nome_arquivo}_Energia_{titulo}.pdf", format='pdf')
    plt.savefig(f"{nome_arquivo}_Energia_{titulo}.png", format='png')
    #plt.show()
