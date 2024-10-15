import numpy as np

def teste_persistencia(var_ant, var_dia_anterior, n_amostras, n):
    # Definição das flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização das variáveis
    persistencia = np.full(n, np.nan)
    
    persistencia_flag6 = 0
    persistencia_flag5 = 0
    persistencia_flag4 = 0
    persistencia_flag3 = 0
    persistencia_flag2 = 0
    persistencia_flag1 = 0

    # Loop de comparação
    for i in range(n):
        if var_ant[i] == flag6:
            persistencia[i] = flag6
            persistencia_flag6 += 1
        elif var_ant[i] == flag5:
            persistencia[i] = flag5
            persistencia_flag5 += 1
        elif var_ant[i] in [flag4, flag3]:
            persistencia[i] = flag4
            persistencia_flag4 += 1
        elif var_ant[i] == flag2:
            persistencia[i] = flag2
            persistencia_flag2 += 1
        else:
            if abs(np.max(var_dia_anterior[i:i+n_amostras]) - np.min(var_dia_anterior[i:i+n_amostras])) != 0:
                persistencia[i] = flag1
                persistencia_flag1 += 1
            else:
                persistencia[i] = flag3
                persistencia_flag3 += 1

    # Preparação dos resultados
    x = persistencia

    y = np.full(6, np.nan)
    y[0] = persistencia_flag1
    y[1] = persistencia_flag2
    y[2] = persistencia_flag3
    y[3] = persistencia_flag4
    y[4] = persistencia_flag5
    y[5] = persistencia_flag6

    return x, y
