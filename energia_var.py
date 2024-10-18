import numpy as np
import pandas as pd

def energia_var(resultado, var_avg, nome_var, n):
    var_pot = np.full(n, np.nan)
    flag1 = 10000

    # Preencher var_pot
    for i in range(n):
        if resultado[i] == flag1:
            var_pot[i] = var_avg[i]

    # Agrupar em faixas
    cont = np.zeros(37, dtype=int)
    
    for value in var_pot:
        if value > 0 and value <= 50:
            cont[0] += 1
        elif value > 50 and value <= 100:
            cont[1] += 1
        elif value > 100 and value <= 150:
            cont[2] += 1
        elif value > 150 and value <= 200:
            cont[3] += 1
        elif value > 200 and value <= 250:
            cont[4] += 1
        elif value > 250 and value <= 300:
            cont[5] += 1
        elif value > 300 and value <= 350:
            cont[6] += 1
        elif value > 350 and value <= 400:
            cont[7] += 1
        elif value > 400 and value <= 450:
            cont[8] += 1
        elif value > 450 and value <= 500:
            cont[9] += 1
        elif value > 500 and value <= 550:
            cont[10] += 1
        elif value > 550 and value <= 600:
            cont[11] += 1
        elif value > 600 and value <= 650:
            cont[12] += 1
        elif value > 650 and value <= 700:
            cont[13] += 1
        elif value > 700 and value <= 750:
            cont[14] += 1
        elif value > 750 and value <= 800:
            cont[15] += 1
        elif value > 800 and value <= 850:
            cont[16] += 1
        elif value > 850 and value <= 900:
            cont[17] += 1
        elif value > 900 and value <= 950:
            cont[18] += 1
        elif value > 950 and value <= 1000:
            cont[19] += 1
        elif value > 1000 and value <= 1050:
            cont[20] += 1
        elif value > 1050 and value <= 1100:
            cont[21] += 1
        elif value > 1100 and value <= 1150:
            cont[22] += 1
        elif value > 1150 and value <= 1200:
            cont[23] += 1
        elif value > 1200 and value <= 1250:
            cont[24] += 1
        elif value > 1250 and value <= 1300:
            cont[25] += 1
        elif value > 1300 and value <= 1350:
            cont[26] += 1
        elif value > 1350 and value <= 1400:
            cont[27] += 1
        elif value > 1400 and value <= 1450:
            cont[28] += 1
        elif value > 1450 and value <= 1500:
            cont[29] += 1
        elif value > 1500 and value <= 1550:
            cont[30] += 1
        elif value > 1550 and value <= 1600:
            cont[31] += 1
        elif value > 1600 and value <= 1650:
            cont[32] += 1
        elif value > 1650 and value <= 1700:
            cont[33] += 1
        elif value > 1700 and value <= 1750:
            cont[34] += 1
        elif value > 1750 and value <= 1800:
            cont[35] += 1
        elif value > 1800:
            cont[36] += 1

    soma_cont = np.sum(cont)
    porcentagem = (cont / soma_cont) * 100

    # Faixas
    faixa = np.arange(0, 1850, 50)
    contx = np.zeros(5, dtype=int)

    for value in var_pot:
        if value <= 300:
            contx[0] += 1
        elif value > 300 and value <= 700:
            contx[1] += 1
        elif value > 700 and value <= 1000:
            contx[2] += 1
        elif value > 1000 and value <= 1200:
            contx[3] += 1
        elif value > 1200:
            contx[4] += 1

    soma_contx = np.sum(contx)
    porcen = (contx / soma_contx) * 100

    faixa2 = ['G <= 300', '300 < G <= 700', '700 < G <= 1000', '1000 < G <= 1200', 'G >= 1200']

    # Exportação para o Excel
    M = np.full((37, 9), np.nan, dtype=object)
    
    # Preencher a primeira coluna com 'DHI'
    M[:, 0] = nome_var
    # Preencher a segunda coluna com as faixas
    M[:, 1] = faixa
    # Preencher a terceira coluna com as contagens
    M[:, 2] = cont
    # Preencher a quarta coluna com as porcentagens
    M[:, 3] = porcentagem

    M[:, 4] = np.nan
    # Preencher a quinta coluna com faixa2, completando com NaN
    M[:5, 5] = faixa2
    # Preencher a sexta coluna com contx
    M[:5, 6] = contx
    # Preencher a sétima coluna com porcen
    M[:5, 7] = porcen

    M[:, 8] = np.nan

    # Criar um DataFrame a partir da matriz
    df = pd.DataFrame(M, columns=[nome_var, 'Faixa', 'Quantidade', 'Porcentagem','', 'Faixa', 'Quantidade', 'Porcentagem', ''])

    # Exportar para Excel
    df.to_excel(f'Energia_{nome_var}.xlsx', index=False)

    # Retornar o DataFrame e o nome do arquivo
    return M, df
