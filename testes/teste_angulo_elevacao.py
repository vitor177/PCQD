import numpy as np

def teste_angulo_elevacao(ant_avg, alpha, n):
    # Definindo Flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização das variáveis para Elevação > 7 GHI
    elevacao7 = np.full(n, np.nan)
    elevacao7_flag6 = 0
    elevacao7_flag5 = 0
    elevacao7_flag4 = 0
    elevacao7_flag3 = 0
    elevacao7_flag2 = 0
    elevacao7_flag1 = 0

    # Loop para Elevação > 7 GHI
    for i in range(n):
        if ant_avg[i] == flag6:
            elevacao7[i] = flag6
            elevacao7_flag6 += 1
        elif ant_avg[i] == flag5:
            elevacao7[i] = flag5
            elevacao7_flag5 += 1
        elif ant_avg[i] in [flag3, flag4]:
            print("VAISF")
            elevacao7[i] = flag4
            elevacao7_flag4 += 1
        else:
            if ant_avg[i] == flag1 and alpha[i] >= 7:
                elevacao7[i] = flag1
                elevacao7_flag1 += 1
            elif ant_avg[i] == flag2 and alpha[i] < 7:
                elevacao7[i] = flag5
                elevacao7_flag5 += 1
            else:
                elevacao7[i] = flag5
                elevacao7_flag5 += 1

    # Resultados X e Y
    x = elevacao7

    y = np.full(6, np.nan)
    y[0] = elevacao7_flag1
    y[1] = elevacao7_flag2
    y[2] = elevacao7_flag3
    y[3] = elevacao7_flag4
    y[4] = elevacao7_flag5
    y[5] = elevacao7_flag6

    return x, y
