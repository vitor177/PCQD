import numpy as np

def teste_std_consistencia(var_ant, var_avg, var_max, var_min, var_std, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= desvio padrão diferente de 0 =======
    desv_pad_0 = np.full(n, np.nan)
    desv_pad_0_flag6 = 0
    desv_pad_0_flag5 = 0
    desv_pad_0_flag4 = 0
    desv_pad_0_flag3 = 0
    desv_pad_0_flag2 = 0
    desv_pad_0_flag1 = 0

    for i in range(n):
        # Verifica se var_ant tem mais de uma coluna
        if var_ant.ndim > 1:
            current_value = var_ant[i, 0]  # Acessa a primeira coluna
        else:
            current_value = var_ant[i]      # Acessa o valor diretamente

        if current_value == flag6:
            desv_pad_0[i] = flag6
            desv_pad_0_flag6 += 1
        else:
            if current_value == flag5:
                desv_pad_0[i] = flag5
                desv_pad_0_flag5 += 1
            elif current_value in (flag4, flag3):
                desv_pad_0[i] = flag4
                desv_pad_0_flag4 += 1
            elif current_value == flag2:
                desv_pad_0[i] = flag2
                desv_pad_0_flag2 += 1
            else:
                if var_avg[i] == flag1 and var_std[i] == 0 and var_avg[i] != 0:
                    desv_pad_0[i] = flag3
                    desv_pad_0_flag3 += 1
                else:
                    desv_pad_0[i] = flag1
                    desv_pad_0_flag1 += 1

    # ======= deriva var =======
    consistencia = np.full(n, np.nan)
    consistencia_flag6 = 0
    consistencia_flag5 = 0
    consistencia_flag4 = 0
    consistencia_flag3 = 0
    consistencia_flag2 = 0
    consistencia_flag1 = 0

    for i in range(n):
        if desv_pad_0[i] == flag6:
            consistencia[i] = flag6
            consistencia_flag6 += 1
        elif desv_pad_0[i] == flag5:
            consistencia[i] = flag5
            consistencia_flag5 += 1
        elif desv_pad_0[i] in (flag4, flag3):
            consistencia[i] = flag4
            consistencia_flag4 += 1
        elif desv_pad_0[i] == flag2:
            consistencia[i] = flag2
            consistencia_flag2 += 1
        else:
            if var_avg[i] >= var_min[i] and var_avg[i] <= var_max[i]:
                consistencia[i] = flag1
                consistencia_flag1 += 1
            else:
                consistencia[i] = flag3
                consistencia_flag3 += 1

    z = 1

    x = np.full((n, 2), np.nan)
    x[:, 0] = desv_pad_0
    x[:, 1] = consistencia

    y = np.full((6, 2), np.nan)
    y[0, 0] = desv_pad_0_flag1
    y[1, 0] = desv_pad_0_flag2
    y[2, 0] = desv_pad_0_flag3
    y[3, 0] = desv_pad_0_flag4
    y[4, 0] = desv_pad_0_flag5
    y[5, 0] = desv_pad_0_flag6

    y[0, 1] = consistencia_flag1
    y[1, 1] = consistencia_flag2
    y[2, 1] = consistencia_flag3
    y[3, 1] = consistencia_flag4
    y[4, 1] = consistencia_flag5
    y[5, 1] = consistencia_flag6

    return x, y
