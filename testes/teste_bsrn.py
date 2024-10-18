import numpy as np

def teste_bsrn(var_ant, var, fpmin, fpmax, ermin, ermax, n):
    # Definindo Flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização das variáveis para "Fisicamente Possível"
    reprovados_fp = np.full(n, np.nan)
    fp = np.full(n, np.nan)
    fp_flag6 = 0
    fp_flag5 = 0
    fp_flag4 = 0
    fp_flag3 = 0
    fp_flag2 = 0
    fp_flag1 = 0

    # Loop para Fisicamente Possível
    for i in range(n):
        if var_ant[i] == flag6:
            fp[i] = flag6
            fp_flag6 += 1
        elif var_ant[i] == flag5:
            fp[i] = flag5
            fp_flag5 += 1
        elif var_ant[i] in [flag4, flag3]:
            fp[i] = flag4
            fp_flag4 += 1
        else:
            if var[i] < fpmin or var[i] > fpmax[i]:
                fp[i] = flag3
                fp_flag3 += 1
                reprovados_fp[i] = var[i]
            else:
                fp[i] = flag1
                fp_flag1 += 1

    # Inicialização das variáveis para "Extremamente Raro"
    reprovados_er = np.full(n, np.nan)
    er = np.full(n, np.nan)
    er_flag6 = 0
    er_flag5 = 0
    er_flag4 = 0
    er_flag3 = 0
    er_flag2 = 0
    er_flag1 = 0


    # Loop para Extremamente Raro
    for i in range(n):
        if fp[i] == flag6:
            er[i] = flag6
            er_flag6 += 1
        elif fp[i] == flag5:
            er[i] = flag5
            er_flag5 += 1
        elif fp[i] in [flag3, flag4]:
            er[i] = flag4
            er_flag4 += 1
        else:
            if var[i] < ermin or var[i] > ermax[i]:
                er[i] = flag2
                er_flag2 += 1
                reprovados_er[i] = var[i]
            else:
                er[i] = flag1
                er_flag1 += 1

    # Resultados X e Y
    x = np.full((n, 2), np.nan)
    x[:, 0] = fp
    x[:, 1] = er

    y = np.full((6, 2), np.nan)
    y[0, 0] = fp_flag1
    y[1, 0] = fp_flag2
    y[2, 0] = fp_flag3
    y[3, 0] = fp_flag4
    y[4, 0] = fp_flag5
    y[5, 0] = fp_flag6

    y[0, 1] = er_flag1
    y[1, 1] = er_flag2
    y[2, 1] = er_flag3
    y[3, 1] = er_flag4
    y[4, 1] = er_flag5
    y[5, 1] = er_flag6

    return x, y
