import numpy as np

def teste_consistencia(var_ant, var, n):

    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Consistência  =======
    consistencia = np.full(n, np.nan)
    consistencia_flag6 = 0
    consistencia_flag5 = 0
    consistencia_flag4 = 0
    consistencia_flag3 = 0
    consistencia_flag2 = 0
    consistencia_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            consistencia[i] = flag6
            consistencia_flag6 += 1
        elif var_ant[i] == flag5:
            consistencia[i] = flag5
            consistencia_flag5 += 1
        elif var_ant[i] == flag4 or var_ant[i] == flag3:
            consistencia[i] = flag4
            consistencia_flag4 += 1
        elif var_ant[i] == flag2:
            consistencia[i] = flag2
            consistencia_flag2 += 1
        else:
            if i < n - 1:
                if (abs(var[i] - var[i + 1]) > 800 and abs(var[i] - var[i + 1]) <= 1000 and var[i + 1] < flag3):
                    consistencia[i] = flag2
                    consistencia_flag2 += 1
                elif abs(var[i] - var[i + 1]) > 1000:
                    consistencia[i] = flag3
                    consistencia_flag3 += 1
                else:
                    consistencia[i] = flag1
                    consistencia_flag1 += 1
            else:
                if ((abs(var[i] - var[i - 1]) > 800 and abs(var[i] - var[i - 1]) <= 1000 and var[i - 1] < flag3) or 
                    (abs(var[i] - var[i + 1]) > 800 and abs(var[i] - var[i + 1]) <= 1000 and var[i - 1] < flag3)):
                    consistencia[i] = flag2
                    consistencia_flag2 += 1
                elif abs(var[i] - var[i - 1]) > 1000 and var[i - 1] < flag3:
                    consistencia[i] = flag3
                    consistencia_flag3 += 1
                elif var[i - 1] < flag3 or var[i + 1] < flag3:
                    consistencia[i] = flag1
                    consistencia_flag1 += 1

    x = np.full(n, np.nan)
    x[:] = consistencia

    y = np.full(6, np.nan)
    y[0] = consistencia_flag1
    y[1] = consistencia_flag2
    y[2] = consistencia_flag3
    y[3] = consistencia_flag4
    y[4] = consistencia_flag5
    y[5] = consistencia_flag6

    return x, y
