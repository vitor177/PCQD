import numpy as np

def teste_kt_ghi(var_ant, ghi_avg, cosazs, iox, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ======= Kt GHI =======
    kt_ghi = np.full(n, np.nan)
    kt_ghi_flag6 = 0
    kt_ghi_flag5 = 0
    kt_ghi_flag4 = 0
    kt_ghi_flag2 = 0
    kt_ghi_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            kt_ghi[i] = flag6
            kt_ghi_flag6 += 1
        elif var_ant[i] == flag5:
            kt_ghi[i] = flag5
            kt_ghi_flag5 += 1
        elif var_ant[i] in (flag4, flag3):
            kt_ghi[i] = flag4
            kt_ghi_flag4 += 1
        elif var_ant[i] == flag2:
            kt_ghi[i] = flag2
            kt_ghi_flag2 += 1
        else:
            if iox[i] == 0:
                kt_ghi[i] = flag5
                kt_ghi_flag5 += 1
            else:
                kt_ghi[i] = ghi_avg[i] / (iox[i] * cosazs[i])
                kt_ghi_flag1 += 1

    # ======= 0 < Kt < 1.2 GHI =======
    zero_kt_12 = np.full(n, np.nan)
    zero_kt_12_flag6 = 0
    zero_kt_12_flag5 = 0
    zero_kt_12_flag4 = 0
    zero_kt_12_flag3 = 0
    zero_kt_12_flag2 = 0
    zero_kt_12_flag1 = 0

    for i in range(n):
        if kt_ghi[i] == flag6:
            zero_kt_12[i] = flag6
            zero_kt_12_flag6 += 1
        elif kt_ghi[i] == flag5:
            zero_kt_12[i] = flag5
            zero_kt_12_flag5 += 1
        elif kt_ghi[i] in (flag4, flag3):
            zero_kt_12[i] = flag4
            zero_kt_12_flag4 += 1
        elif kt_ghi[i] == flag2:
            zero_kt_12[i] = flag2
            zero_kt_12_flag2 += 1
        else:
            if kt_ghi[i] < 0 or kt_ghi[i] > 1.2:
                zero_kt_12[i] = flag3
                zero_kt_12_flag3 += 1
            else:
                zero_kt_12[i] = flag1
                zero_kt_12_flag1 += 1

    X = np.full((n, 2), np.nan)
    X[:, 0] = kt_ghi
    X[:, 1] = zero_kt_12

    Y = np.full((6, 2), np.nan)
    Y[0, 0] = kt_ghi_flag1
    Y[1, 0] = kt_ghi_flag2
    Y[3, 0] = kt_ghi_flag4
    Y[4, 0] = kt_ghi_flag5
    Y[5, 0] = kt_ghi_flag6

    Y[0, 1] = zero_kt_12_flag1
    Y[1, 1] = zero_kt_12_flag2
    Y[2, 1] = zero_kt_12_flag3
    Y[3, 1] = zero_kt_12_flag4
    Y[4, 1] = zero_kt_12_flag5
    Y[5, 1] = zero_kt_12_flag6

    return X, Y
