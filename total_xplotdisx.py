import numpy as np
import matplotlib.pyplot as plt

def total_xplotdisx(var1, var2, nome1, nome2, unid, fig, lim, nome_arquivo):
    n = len(var1)

    # Inicializando arrays aux1 e aux2
    aux1 = np.full(n, np.nan)
    aux2 = np.full(n, np.nan)

    # Filtrando valores não negativos
    for i in range(n):
        if var1[i] >= 0 and var2[i] >= 0:
            aux1[i] = var1[i]
            aux2[i] = var2[i]

    var1 = aux1[~np.isnan(aux1)]  # Removendo NaNs
    var2 = aux2[~np.isnan(aux2)]  # Removendo NaNs

    # Ajuste de mínimos quadrados
    A = np.column_stack((var2, np.ones(var2.shape)))  # Adiciona a coluna de bias
    th = np.linalg.inv(A.T @ A) @ A.T @ var1  # (A'A)^-1.A'.b = x
    y_fit = A @ th  # Valores ajustados

    # Coeficiente de determinação R^2
    y_resid = var1 - y_fit
    sq_resid = np.sum(y_resid ** 2)
    sq_total = (len(var1) - 1) * np.var(var1)
    r_squared = 1 - sq_resid / sq_total

    # Criando o gráfico
    plt.figure(fig + 50, figsize=(7, 6))
    plt.plot(var2, var1, 'ko', label='Dados')
    plt.plot(var2, y_fit, linewidth=2, color='r', label='Ajuste Linear')
    
    plt.grid(True)
    plt.title(f'Dispersão entre {nome1} e {nome2}')
    plt.ylim([0, lim])
    plt.xlim([0, lim])
    plt.xticks(np.arange(0, lim + 1, lim / 10))
    plt.yticks(np.arange(0, lim + 1, lim / 10))
    plt.ylabel(f'{nome1} {unid}')
    plt.xlabel(f'{nome2} {unid}')
    plt.gca().set_xticks(np.arange(0, lim + 1, lim / 10))
    plt.gca().set_yticks(np.arange(0, lim + 1, lim / 10))
    plt.gca().tick_params(labelsize=10)
    
    # Salvando os gráficos como PDF e PNG
    plt.savefig(f"{nome_arquivo}_{nome1} xA {nome2}.pdf", format='pdf')
    plt.savefig(f"{nome_arquivo}_{nome1} xA {nome2}.png", format='png')
    
    # Exibindo o gráfico
    plt.show()
    
    return r_squared  # Retornando R^2, se necessário

