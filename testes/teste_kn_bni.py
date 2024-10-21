import numpy as np

def teste_kn_bni(var_ant, bni_avg, iox, n):

    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Kn BNI =======
    kn_bni = np.full(n, np.nan)
    kn_bni_flag6 = 0
    kn_bni_flag5 = 0
    kn_bni_flag4 = 0
    kn_bni_flag2 = 0
    kn_bni_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            kn_bni[i] = flag6
            kn_bni_flag6 += 1
        elif var_ant[i] == flag5:
            kn_bni[i] = flag5
            kn_bni_flag5 += 1
        elif var_ant[i] == flag4 or var_ant[i] == flag3:
            kn_bni[i] = flag4
            kn_bni_flag4 += 1
        elif var_ant[i] == flag2:
            kn_bni[i] = flag2
            kn_bni_flag2 += 1
        else:
            if iox[i] == 0:
                kn_bni[i] = flag5
                kn_bni_flag5 += 1
            else:
                kn_bni[i] = bni_avg[i] / iox[i]
                kn_bni_flag1 += 1

    # ======= 0 < Kn < 1.1 GHI =======
    zero_kn_11 = np.full(n, np.nan)
    zero_kn_11_flag6 = 0
    zero_kn_11_flag5 = 0
    zero_kn_11_flag4 = 0
    zero_kn_11_flag3 = 0
    zero_kn_11_flag2 = 0
    zero_kn_11_flag1 = 0

    for i in range(n):
        if kn_bni[i] == flag6:
            zero_kn_11[i] = flag6
            zero_kn_11_flag6 += 1
        elif kn_bni[i] == flag5:
            zero_kn_11[i] = flag5
            zero_kn_11_flag5 += 1
        elif kn_bni[i] == flag4 or kn_bni[i] == flag3:
            zero_kn_11[i] = flag4
            zero_kn_11_flag4 += 1
        elif kn_bni[i] == flag2:
            zero_kn_11[i] = flag2
            zero_kn_11_flag2 += 1
        else:
            if kn_bni[i] < 0 or kn_bni[i] > 1.5:
                zero_kn_11[i] = flag3
                zero_kn_11_flag3 += 1
            else:
                zero_kn_11[i] = flag1
                zero_kn_11_flag1 += 1

    x = np.full((n, 2), np.nan)
    x[:, 0] = kn_bni
    x[:, 1] = zero_kn_11

    y = np.full((6, 2), np.nan)
    y[0, 0] = kn_bni_flag1
    y[1, 0] = kn_bni_flag2
    y[3, 0] = kn_bni_flag4
    y[4, 0] = kn_bni_flag5
    y[5, 0] = kn_bni_flag6

    y[0, 1] = zero_kn_11_flag1
    y[1, 1] = zero_kn_11_flag2
    y[2, 1] = zero_kn_11_flag3
    y[3, 1] = zero_kn_11_flag4
    y[4, 1] = zero_kn_11_flag5
    y[5, 1] = zero_kn_11_flag6

    return x, y
