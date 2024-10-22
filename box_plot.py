import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def blox_plot(resultado, var, nome_arquivo, nome_var, num_figura, und, limiy, limsy, n):
    var_x = np.full((n, 1), np.nan)

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
    # (Aqui você pode manter seu código anterior para calcular estatísticas)

    #------------------------------------------------------
    #                      Plot Bloxplot com Seaborn
    #------------------------------------------------------

    plt.figure(num_figura, figsize=(4, 6))
    sns.boxplot(data=var_y, whis=2.5, width=0.75)

    mean_value = np.nanmean(var_y)
    plt.plot(1, mean_value, 'ko', markersize=10, markerfacecolor='k', label='Média')

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
    plt.text(1.1, mean_value, f'{mean_value:.2f}', fontsize=15, verticalalignment='bottom')

    # Salvando o gráfico
    plt.savefig(f'{nome_arquivo}_bloxplot_{nome_var}.pdf', format='pdf')
    plt.savefig(f'{nome_arquivo}_bloxplot_{nome_var}.png', format='png')

    #plt.show()  # Exibe o gráfico

    return
