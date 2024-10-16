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

    # Exportação para o Excel
    M = np.full((37, 4), np.nan)
    M[:, 0] = cont
    M[:, 1] = porcentagem
    M[:5, 2] = contx
    M[:5, 3] = porcen

    M = pd.DataFrame(M, columns=['Quantidade', 'Porcentagem', '', ''])
    faixa_df = pd.DataFrame({'Faixa': faixa})
    faixa2 = ['G <= 300', '300 < G <= 700', '700 < G <= 1000', '1000 < G <= 1200', 'G >= 1200']

    XLSX = pd.concat([
        faixa_df, M.iloc[:, :2],
        pd.DataFrame({faixa2[i]: [contx[i]] for i in range(len(faixa2))}),
        pd.DataFrame({'Porcentagem': porcen})
    ], axis=1)

    XLSX.to_excel('Energia.xlsx', index=False)

    return M.values, XLSX

# Exemplo de uso
# resultado = np.random.randint(0, 20000, size=(100, 1))
# var_avg = np.random.uniform(0, 2000, size=(100, 1))
# nome_var = "Variável de Energia"
# n = 100
# M, XLSX = energia_var(resultado, var_avg, nome_var, n)