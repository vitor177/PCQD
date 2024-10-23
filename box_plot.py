import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def blox_plot(resultado, var, nome_arquivo, nome_var, num_figura, und, limiy, limsy, n):
    # Cria uma nova figura
    plt.figure(num_figura, figsize=(8, 4))
    
    var_x = np.full(n, np.nan)

    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Filtra os valores de Var que atendem à condição
    for i in range(n):
        if resultado[i] != flag6 and resultado[i] != flag3:
            var_x[i] = var[i]

    # Tratando valores de Var_x para eliminar valores acima de 1000
    var_y = np.copy(var_x)
    var_x[var_x > 1000] = 0
    var_y[var_y > 1000] = np.nan

    # Calcular estatísticas
    quartil_sup = np.nanquantile(var_y, 0.75)
    max_var = np.nanmax(var_x)
    mediana_var = np.nanmedian(var_y)
    media_var = np.nanmean(var_y)
    min_var = np.nanmin(var_y)
    quartil_inf = np.nanquantile(var_y, 0.25)
    std_var = np.nanstd(var_y)

# Criando a matriz O
    O = np.array([nome_var, quartil_sup, max_var, mediana_var, media_var, min_var, quartil_inf, std_var])

# Corrigindo aqui para empilhar nome_var
    #O = np.column_stack((np.array([nome_var]), O))  # Adiciona o nome da variável como uma nova linha


    #------------------------------------------------------
    #                      Plot Bloxplot com Seaborn
    #------------------------------------------------------
    sns.boxplot(data=var_y, whis=2.5, width=0.75)

    plt.plot(1, media_var, 'ko', markersize=10, markerfacecolor='k', label='Média')

    # Configurando título e rótulos
    plt.title(nome_arquivo, fontsize=15)
    plt.ylabel(und, fontsize=15)
    plt.xlabel(nome_var, fontsize=15)
    plt.ylim([limiy, limsy])
    plt.grid(True)

    # Removendo valores do eixo X
    plt.xticks([])

    # Exibindo valores mínimo, máximo e média no gráfico
    plt.text(1.1, np.nanmin(var_y), f'{np.nanmin(var_y):.2f}', fontsize=15, verticalalignment='bottom')
    plt.text(1.1, np.nanmax(var_y), f'{np.nanmax(var_y):.2f}', fontsize=15, verticalalignment='bottom')
    plt.text(1.1, media_var, f'{media_var:.2f}', fontsize=15, verticalalignment='bottom')

    # Salvando o gráfico
    plt.savefig(f'{nome_arquivo}_bloxplot_{nome_var}.pdf', format='pdf')
    plt.savefig(f'{nome_arquivo}_bloxplot_{nome_var}.png', format='png')

    plt.clf()  # Limpa a figura atual para liberar memória
    return O   # Retorna a matriz O
