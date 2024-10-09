import numpy as np

def teste_limites_fisicos(var, var_ant, lims, limi, n):
    # Definindo Flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização das variáveis
    lf = np.full(n, np.nan)
    lf_flag6 = 0
    lf_flag5 = 0
    lf_flag4 = 0
    lf_flag3 = 0
    lf_flag2 = 0
    lf_flag1 = 0
    flag3x = np.full(n, np.nan)

    # Loop para verificação das condições
    for i in range(n):
        if var_ant[i] == flag6:
            lf[i] = flag6
            lf_flag6 += 1
        elif var_ant[i] == flag5:
            lf[i] = flag5
            lf_flag5 += 1
        elif var_ant[i] == flag4:
            lf[i] = flag4
            lf_flag4 += 1
        elif var_ant[i] == flag2:
            lf[i] = flag2
            lf_flag2 += 1
        else:
            if limi < var_ant[i] < lims:
                lf[i] = flag3
                lf_flag3 += 1
                flag3x[i] = var[i]
            else:
                lf[i] = flag1
                lf_flag1 += 1

    x = lf

    # Resultados das flags
    y = np.full(6, np.nan)
    y[0] = lf_flag1
    y[1] = lf_flag2
    y[2] = lf_flag3
    y[3] = lf_flag4
    y[4] = lf_flag5
    y[5] = lf_flag6

    return x, y
