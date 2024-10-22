import numpy as np

def teste_evolucao_temporal(var, var_ant, var_dia, dia_anterior, lim_m, tempo, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Evolução Temporal =======
    et_t = np.full(n, np.nan)

    for i in range(n):
        et_t[i] = abs(np.max(var_dia[dia_anterior + i - tempo:dia_anterior + i]) -
                         np.min(var_dia[dia_anterior + i - tempo:dia_anterior + i]))
        if et_t[i] >= flag5:
            et_t[i] = flag5

    # ======= Evolução Temporal -> Validação =======
    et = np.full(n, np.nan)
    et_flag6 = 0
    et_flag5 = 0
    et_flag4 = 0
    et_flag3 = 0
    et_flag2 = 0
    et_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            et[i] = flag6
            et_flag6 += 1
        elif var_ant[i] == flag5:
            et[i] = flag5
            et_flag5 += 1
        elif var_ant[i] == flag4:
            et[i] = flag4
            et_flag4 += 1
        elif var_ant[i] == flag2:
            et[i] = flag2
            et_flag2 += 1
        else:
            if et_t[i] > lim_m:
                et[i] = flag1
                et_flag1 += 1
            else:
                et[i] = flag3
                et_flag3 += 1

    x = et

    y = np.full(6, np.nan)
    y[0] = et_flag1
    y[1] = et_flag2
    y[2] = et_flag3
    y[3] = et_flag4
    y[4] = et_flag5
    y[5] = et_flag6

    return x, y
