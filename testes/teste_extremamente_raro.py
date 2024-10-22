import numpy as np

def teste_extremamente_raro(var, var_ant, var_dia, dia_anterior, lim_m, tempo, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Extremamente Raro =======
    er_t = np.full(n, np.nan)

    for i in range(n):
        er_t[i] = abs(np.max(var_dia[dia_anterior + i - tempo + 1:dia_anterior + i]) - 
                         np.min(var_dia[dia_anterior + i - tempo + 1:dia_anterior + i]))
        if er_t[i] >= flag5:
            er_t[i] = flag5

    # ======= Extremamente Raro -> Validação =======
    er = np.full(n, np.nan)
    er_flag6 = 0
    er_flag5 = 0
    er_flag4 = 0
    er_flag3 = 0
    er_flag2 = 0
    er_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            er[i] = flag6
            er_flag6 += 1
        elif var_ant[i] == flag5:
            er[i] = flag5
            er_flag5 += 1
        elif var_ant[i] == flag4:
            er[i] = flag4
            er_flag4 += 1
        elif var_ant[i] == flag2:
            er[i] = flag2
            er_flag2 += 1
        else:
            if er_t[i] < lim_m:
                er[i] = flag1
                er_flag1 += 1
            else:
                er[i] = flag2
                er_flag2 += 1

    x = er

    y = np.full(6, np.nan)
    y[0] = er_flag1
    y[1] = er_flag2
    y[2] = er_flag3
    y[3] = er_flag4
    y[4] = er_flag5
    y[5] = er_flag6

    return x, y
