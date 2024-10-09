import numpy as np

def teste_comparacao_completo(var_ant, ghi, dhi, bni, cos_azs, azs, sky, n):
    # Definições de constantes
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # Inicialização de arrays
    dhi_bhi = np.full(n, np.nan)
    ghi_dhi_bni = np.full(n, np.nan)
    bni_cosz = np.full(n, np.nan)
    dhi_ghi = np.full(n, np.nan)

    for i in range(n):
        dhi_bhi[i] = dhi[i] + (bni[i] * cos_azs[i])
        ghi_dhi_bni[i] = ghi[i] / dhi_bhi[i]
        bni_cosz[i] = bni[i] * cos_azs[i]
        dhi_ghi[i] = dhi[i] / ghi[i]

    # Comparação GHI
    comp_ghi = np.full(n, np.nan)
    comp_ghi_flag_counts = np.zeros(6)

    for i in range(n):
        if var_ant[i] == flag6:
            comp_ghi[i] = flag6
            comp_ghi_flag_counts[5] += 1
        elif var_ant[i] == flag5:
            comp_ghi[i] = flag5
            comp_ghi_flag_counts[4] += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_ghi[i] = flag4
            comp_ghi_flag_counts[3] += 1
        elif var_ant[i] == flag2:
            comp_ghi[i] = flag2
            comp_ghi_flag_counts[2] += 1
        else:
            if bni[i] == flag6 or dhi[i] == flag6:
                comp_ghi[i] = flag5
                comp_ghi_flag_counts[4] += 1
            else:
                if (75 < azs[i] < 93 and dhi_bhi[i] > 50 and
                        0.85 <= abs(ghi_dhi_bni[i]) <= 1.15):
                    comp_ghi[i] = flag1
                    comp_ghi_flag_counts[0] += 1
                elif (azs[i] < 75 and dhi_bhi[i] > 50 and
                        0.90 <= abs(ghi_dhi_bni[i]) <= 1.1):
                    comp_ghi[i] = flag1
                    comp_ghi_flag_counts[0] += 1
                elif (75 < azs[i] < 93 and dhi_bhi[i] > 50 and
                        (abs(ghi_dhi_bni[i]) > 1.15 or
                        abs(ghi_dhi_bni[i]) < 0.85)):
                    comp_ghi[i] = flag2
                    comp_ghi_flag_counts[1] += 1
                elif (azs[i] < 75 and dhi_bhi[i] > 50 and
                        (abs(ghi_dhi_bni[i]) > 1.1 or
                        abs(ghi_dhi_bni[i]) < 0.9)):
                    comp_ghi[i] = flag2
                    comp_ghi_flag_counts[1] += 1
                else:
                    comp_ghi[i] = flag2
                    comp_ghi_flag_counts[1] += 1

    # Comparação BNI
    comp_bni = np.full(n, np.nan)
    aux_bni = np.full(n, np.nan)
    comp_bni_flag_counts = np.zeros(6)

    for i in range(n):
        if var_ant[i] == flag6:
            comp_bni[i] = flag6
            comp_bni_flag_counts[5] += 1
        elif var_ant[i] == flag5:
            comp_bni[i] = flag5
            comp_bni_flag_counts[4] += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_bni[i] = flag4
            comp_bni_flag_counts[3] += 1
        elif var_ant[i] == flag2:
            comp_bni[i] = flag2
            comp_bni_flag_counts[2] += 1
        else:
            if bni[i] == flag6 or ghi[i] == flag6:
                comp_bni[i] = flag5
                comp_bni_flag_counts[4] += 1
            else:
                if (bni_cosz[i] - 50 <= ghi[i] - dhi[i] <= 
                        bni_cosz[i] + 50):
                    comp_bni[i] = flag1
                    comp_bni_flag_counts[0] += 1
                else:
                    comp_bni[i] = flag2
                    comp_bni_flag_counts[1] += 1
                    aux_bni[i] = bni_cosz[i]

    # Comparação DHI
    comp_dhi = np.full(n, np.nan)
    comp_dhi_flag_counts = np.zeros(6)

    for i in range(n):
        if var_ant[i] == flag6:
            comp_dhi[i] = flag6
            comp_dhi_flag_counts[5] += 1
        elif var_ant[i] == flag5:
            comp_dhi[i] = flag5
            comp_dhi_flag_counts[4] += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_dhi[i] = flag4
            comp_dhi_flag_counts[3] += 1
        elif var_ant[i] == flag2:
            comp_dhi[i] = flag2
            comp_dhi_flag_counts[2] += 1
        else:
            if bni[i] == flag6 or ghi[i] == flag6:
                comp_dhi[i] = flag5
                comp_dhi_flag_counts[4] += 1
            else:
                if (75 < azs[i] < 93 and ghi[i] >= 50 and dhi_ghi[i] < 1.1):
                    comp_dhi[i] = flag1
                    comp_dhi_flag_counts[0] += 1
                elif (azs[i] < 75 and ghi[i] >= 50 and dhi_ghi[i] < 1.05):
                    comp_dhi[i] = flag1
                    comp_dhi_flag_counts[0] += 1
                elif ghi[i] < 50:
                    comp_dhi[i] = flag5
                    comp_dhi_flag_counts[4] += 1
                else:
                    comp_dhi[i] = flag2
                    comp_dhi_flag_counts[1] += 1

    # Resultados
    x = np.hstack((comp_ghi, comp_dhi, comp_bni)) # ANALISAR
    y = np.zeros((6, 3))

    # Preenchendo Y com contagens
    for j in range(6):
        y[j] = comp_ghi_flag_counts[j]
        y[j] = comp_dhi_flag_counts[j]
        y[j] = comp_bni_flag_counts[j]

    return x, y
