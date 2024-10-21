import numpy as np

def teste_clear_sky(var_ant, var, mcc_clear, n):

    # Definição das flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização das variáveis
    clear_sky = np.full(n, np.nan)
    aux = np.full(n, np.nan)
    
    clear_sky_flag6 = 0
    clear_sky_flag5 = 0
    clear_sky_flag4 = 0
    clear_sky_flag3 = 0
    clear_sky_flag2 = 0
    clear_sky_flag1 = 0

    # Verificar quantas dimensões tem var_ant
    is_2d = len(var_ant.shape) == 2

    # Loop de comparação
    for i in range(n):
        # Usar [i, 0] se for 2D, caso contrário usar [i]
        if (var_ant[i, 0] if is_2d else var_ant[i]) == flag6:
            clear_sky[i] = flag6
            clear_sky_flag6 += 1
        elif (var_ant[i, 0] if is_2d else var_ant[i]) == flag5:
            clear_sky[i] = flag5
            clear_sky_flag5 += 1
        elif (var_ant[i, 0] if is_2d else var_ant[i]) in [flag4, flag3]:
            clear_sky[i] = flag4
            clear_sky_flag4 += 1
        elif (var_ant[i, 0] if is_2d else var_ant[i]) == flag2:
            clear_sky[i] = flag2
            clear_sky_flag2 += 1
        else:
            if var[i] > mcc_clear[i]:
                clear_sky[i] = flag2
                clear_sky_flag2 += 1
                aux[i] = var[i]
            else:
                clear_sky[i] = flag1
                clear_sky_flag1 += 1

    # Preparação dos resultados
    x = clear_sky

    y = np.full(6, np.nan)
    y[0] = clear_sky_flag1
    y[1] = clear_sky_flag2
    y[2] = clear_sky_flag3
    y[3] = clear_sky_flag4
    y[4] = clear_sky_flag5
    y[5] = clear_sky_flag6

    return x, y
