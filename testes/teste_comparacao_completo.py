import numpy as np

def teste_comparacao_completo(var_ant, ghi, dhi, bni, cosazs, azs, sky, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000
    
    dhi_bhi = np.full(n, np.nan)
    ghi_dhi_bni = np.full(n, np.nan)
    bni_cosz = np.full(n, np.nan)
    dhi_ghi = np.full(n, np.nan)

    for i in range(n):
        dhi_bhi[i] = dhi[i] + (bni[i] * cosazs[i])
        
        # Verificação para evitar divisão por zero
        if dhi_bhi[i] != 0:
            ghi_dhi_bni[i] = ghi[i] / dhi_bhi[i]
        else:
            ghi_dhi_bni[i] = np.nan  # ou 0, dependendo da lógica que você deseja

        bni_cosz[i] = bni[i] * cosazs[i]
        
        # Verificação para evitar divisão por zero
        if ghi[i] != 0:
            dhi_ghi[i] = dhi[i] / ghi[i]
        else:
            dhi_ghi[i] = np.nan  # ou 0, dependendo da lógica que você deseja

    # ========================== Comparação GHI ================================
    comp_ghi = np.full(n, np.nan)
    comp_ghi_flag6 = 0
    comp_ghi_flag5 = 0
    comp_ghi_flag4 = 0
    comp_ghi_flag3 = 0
    comp_ghi_flag2 = 0
    comp_ghi_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            comp_ghi[i] = flag6
            comp_ghi_flag6 += 1
        elif var_ant[i] == flag5:
            comp_ghi[i] = flag5
            comp_ghi_flag5 += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_ghi[i] = flag4
            comp_ghi_flag4 += 1
        elif var_ant[i] == flag2:
            comp_ghi[i] = flag2
            comp_ghi_flag2 += 1
        else:
            if bni[i] == flag6 or dhi[i] == flag6:
                comp_ghi[i] = flag5
                comp_ghi_flag5 += 1
            else:
                if (75 < azs[i] < 93 and dhi_bhi[i] > 50 and
                    0.85 <= abs(ghi_dhi_bni[i]) <= 1.15) or (
                    azs[i] < 75 and dhi_bhi[i] > 50 and
                    0.90 <= abs(ghi_dhi_bni[i]) <= 1.1):
                    comp_ghi[i] = flag1
                    comp_ghi_flag1 += 1
                elif (75 < azs[i] < 93 and dhi_bhi[i] > 50 and
                      (abs(ghi_dhi_bni[i]) < 0.85 or abs(ghi_dhi_bni[i]) > 1.15)) or (
                      azs[i] < 75 and dhi_bhi[i] > 50 and
                      (abs(ghi_dhi_bni[i]) < 0.90 or abs(ghi_dhi_bni[i]) > 1.1)):
                    comp_ghi[i] = flag2
                    comp_ghi_flag2 += 1
                else:
                    comp_ghi[i] = flag2
                    comp_ghi_flag2 += 1

    # ========================== Comparação BNI ================================
    comp_bni = np.full(n, np.nan)
    aux_bni = np.full(n, np.nan)
    comp_bni_flag6 = 0
    comp_bni_flag5 = 0
    comp_bni_flag4 = 0
    comp_bni_flag3 = 0
    comp_bni_flag2 = 0
    comp_bni_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            comp_bni[i] = flag6
            comp_bni_flag6 += 1
        elif var_ant[i] == flag5:
            comp_bni[i] = flag5
            comp_bni_flag5 += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_bni[i] = flag4
            comp_bni_flag4 += 1
        elif var_ant[i] == flag2:
            comp_bni[i] = flag2
            comp_bni_flag2 += 1
        else:
            if ghi[i] == flag6 or dhi[i] == flag6:
                comp_bni[i] = flag5
                comp_bni_flag5 += 1
            else:
                if (bni_cosz[i] - 50 <= ghi[i] - dhi[i] <=
                    bni_cosz[i] + 50):
                    comp_bni[i] = flag1
                    comp_bni_flag1 += 1
                else:
                    comp_bni[i] = flag2
                    comp_bni_flag2 += 1
                    aux_bni[i] = bni_cosz[i]

    # ========================== Comparação DHI ================================
    comp_dhi = np.full(n, np.nan)
    comp_dhi_flag6 = 0
    comp_dhi_flag5 = 0
    comp_dhi_flag4 = 0
    comp_dhi_flag3 = 0
    comp_dhi_flag2 = 0
    comp_dhi_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            comp_dhi[i] = flag6
            comp_dhi_flag6 += 1
        elif var_ant[i] == flag5:
            comp_dhi[i] = flag5
            comp_dhi_flag5 += 1
        elif var_ant[i] in [flag4, flag3]:
            comp_dhi[i] = flag4
            comp_dhi_flag4 += 1
        elif var_ant[i] == flag2:
            comp_dhi[i] = flag2
            comp_dhi_flag2 += 1
        else:
            if bni[i] == flag6 or ghi[i] == flag6:
                comp_dhi[i] = flag5
                comp_dhi_flag5 += 1
            else:
                if (75 < azs[i] < 93 and ghi[i] >= 50 and dhi_ghi[i] < 1.1) or (
                    azs[i] < 75 and ghi[i] >= 50 and dhi_ghi[i] < 1.05):
                    comp_dhi[i] = flag1
                    comp_dhi_flag1 += 1
                elif ghi[i] < 50:
                    comp_dhi[i] = flag5
                    comp_dhi_flag5 += 1
                else:
                    comp_dhi[i] = flag2
                    comp_dhi_flag2 += 1
                    #aux[i] = dhi_ghi[i]

    # ==========================================================================
    
    x = np.full((n, 3), np.nan)
    x[:, 0] = comp_ghi
    x[:, 1] = comp_dhi
    x[:, 2] = comp_bni

    y = np.full((6, 3), np.nan)

    y[0, 0] = comp_ghi_flag1
    y[1, 0] = comp_ghi_flag2
    y[2, 0] = comp_ghi_flag3
    y[3, 0] = comp_ghi_flag4
    y[4, 0] = comp_ghi_flag5
    y[5, 0] = comp_ghi_flag6

    y[0, 1] = comp_dhi_flag1
    y[1, 1] = comp_dhi_flag2
    y[2, 1] = comp_dhi_flag3
    y[3, 1] = comp_dhi_flag4
    y[4, 1] = comp_dhi_flag5
    y[5, 1] = comp_dhi_flag6

    y[0, 2] = comp_bni_flag1
    y[1, 2] = comp_bni_flag2
    y[2, 2] = comp_bni_flag3
    y[3, 2] = comp_bni_flag4
    y[4, 2] = comp_bni_flag5
    y[5, 2] = comp_bni_flag6

    return x, y
