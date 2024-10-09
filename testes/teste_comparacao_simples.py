import numpy as np

def teste_comparacao_simples(var_ref, var_2, var_3, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    comp = np.full(n, np.nan)
    comp_flag6 = 0
    comp_flag5 = 0
    comp_flag4 = 0
    comp_flag3 = 0
    comp_flag2 = 0
    comp_flag1 = 0

    if var_3 is not None and len(var_3) > 0:
        for i in range(n):
            if var_ref[i] == flag6:
                comp[i] = flag6
                comp_flag6 += 1
            elif var_ref[i] == flag5:
                comp[i] = flag5
                comp_flag5 += 1
            elif var_ref[i] == flag4 or var_ref[i] == flag3:
                comp[i] = flag4
                comp_flag4 += 1
            elif var_ref[i] == flag2:
                comp[i] = flag2
                comp_flag2 += 1
            elif abs((var_ref[i] - var_2[i]) / var_ref[i]) < 0.95 and abs((var_ref[i] - var_3[i]) / var_ref[i]) < 0.95:
                comp[i] = flag2
                comp_flag2 += 1
            else:
                comp[i] = flag1
                comp_flag1 += 1
    else:
        for i in range(n):
            if var_ref[i] == flag6:
                comp[i] = flag6
                comp_flag6 += 1
            elif var_ref[i] == flag5:
                comp[i] = flag5
                comp_flag5 += 1
            elif var_ref[i] == flag4 or var_ref[i] == flag3:
                comp[i] = flag4
                comp_flag4 += 1
            elif var_ref[i] == flag2:
                comp[i] = flag2
                comp_flag2 += 1
            elif abs((var_ref[i] - var_2[i]) / var_ref[i]) < 0.05:
                comp[i] = flag2
                comp_flag2 += 1
            else:
                comp[i] = flag1
                comp_flag1 += 1
    x = np.full(n, np.nan)
    x = comp
    y = np.full(6, np.nan)
    y[0] = comp_flag1
    y[1] = comp_flag2
    y[2] = comp_flag3
    y[3] = comp_flag4
    y[4] = comp_flag5
    y[5] = comp_flag6

    return x, y
