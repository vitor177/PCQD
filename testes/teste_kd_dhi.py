import numpy as np

def teste_kd_dhi(var_ant, dhi_avg, ghi_avg, iox, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Kt GHI =======
    kd_dhi = np.full(n, np.nan)
    kd_dhi_flag6 = 0
    kd_dhi_flag5 = 0
    kd_dhi_flag4 = 0
    kd_dhi_flag2 = 0
    kd_dhi_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            kd_dhi[i] = flag6
            kd_dhi_flag6 += 1
        elif var_ant[i] == flag5:
            kd_dhi[i] = flag5
            kd_dhi_flag5 += 1
        elif var_ant[i] == flag4 or var_ant[i] == flag3:
            kd_dhi[i] = flag4
            kd_dhi_flag4 += 1
        elif var_ant[i] == flag2:
            kd_dhi[i] = flag2
            kd_dhi_flag2 += 1
        else:
            if iox[i] == 0:
                kd_dhi[i] = flag5
                kd_dhi_flag5 += 1
            else:
                kd_dhi[i] = dhi_avg[i] / ghi_avg[i]
                kd_dhi_flag1 += 1

    # ======= 0 < Kd < 1,1 DHI =======
    zero_kd_11 = np.full(n, np.nan)
    aux = np.full(n, np.nan)
    zero_kd_11_flag6 = 0
    zero_kd_11_flag5 = 0
    zero_kd_11_flag4 = 0
    zero_kd_11_flag3 = 0
    zero_kd_11_flag2 = 0
    zero_kd_11_flag1 = 0

    for i in range(n):
        if kd_dhi[i] == flag6:
            zero_kd_11[i] = flag6
            zero_kd_11_flag6 += 1
        elif kd_dhi[i] == flag5:
            zero_kd_11[i] = flag5
            zero_kd_11_flag5 += 1
        elif kd_dhi[i] == flag4 or kd_dhi[i] == flag3:
            zero_kd_11[i] = flag4
            zero_kd_11_flag4 += 1
        elif kd_dhi[i] == flag2:
            zero_kd_11[i] = flag2
            zero_kd_11_flag2 += 1
        else:
            if kd_dhi[i] < 0 or kd_dhi[i] > 1.1:
                zero_kd_11[i] = flag3
                zero_kd_11_flag3 += 1
            else:
                zero_kd_11[i] = flag1
                zero_kd_11_flag1 += 1

    # Saída X e Y
    x = np.full((n, 2), np.nan)
    x[:, 0] = kd_dhi
    x[:, 1] = zero_kd_11

    y = np.full((6, 2), np.nan)
    y[0, 0] = kd_dhi_flag1
    y[1, 0] = kd_dhi_flag2
    y[3, 0] = kd_dhi_flag4
    y[4, 0] = kd_dhi_flag5
    y[5, 0] = kd_dhi_flag6

    y[0, 1] = zero_kd_11_flag1
    y[1, 1] = zero_kd_11_flag2
    y[2, 1] = zero_kd_11_flag3
    y[3, 1] = zero_kd_11_flag4
    y[4, 1] = zero_kd_11_flag5
    y[5, 1] = zero_kd_11_flag6

    return x, y
