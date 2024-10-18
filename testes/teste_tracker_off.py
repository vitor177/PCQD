import numpy as np

def teste_tracker_off(var, ghi, dhi, bni, cosazs, azs, ghi_mcc_clear, n):
    # definindo as flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # inicializando as variáveis
    tracker_off = np.full(n, np.nan)
    tracker_off_flag6 = 0
    tracker_off_flag5 = 0
    tracker_off_flag4 = 0
    tracker_off_flag3 = 0
    tracker_off_flag2 = 0
    tracker_off_flag1 = 0

    dhi_bhi_ghicc = np.full(n, np.nan)
    dhi_ghi = np.full(n, np.nan)

    # loop principal
    for i in range(n):
        # Tratamento de divisões por zero
        if cosazs[i] != 0 and ghi_mcc_clear[i] != 0:
            dhi_bhi_ghicc[i] = (dhi[i] + (bni[i] / cosazs[i])) / ghi_mcc_clear[i]
        else:
            dhi_bhi_ghicc[i] = 0

        if ghi[i] != 0:
            dhi_ghi[i] = dhi[i] / ghi[i]
        else:
            dhi_ghi[i] = 0

        if var[i, 0] == flag6:
            tracker_off[i] = flag6
            tracker_off_flag6 += 1
        elif var[i, 0] == flag5:
            tracker_off[i] = flag5
            tracker_off_flag5 += 1
        elif var[i, 0] == flag4 or var[i, 0] == flag3:
            tracker_off[i] = flag4
            tracker_off_flag4 += 1
        elif var[i, 0] == flag2:
            tracker_off[i] = flag2
            tracker_off_flag2 += 1
        else:
            if dhi_bhi_ghicc[i] < 0.85 and dhi_ghi[i] < 0.85 and bni[i] > 50 and azs[i] < 75:
                tracker_off[i] = flag2
                tracker_off_flag2 += 1
            else:
                tracker_off[i] = flag1
                tracker_off_flag1 += 1

    # saídas x e y
    x = tracker_off

    y = np.full(6, np.nan)
    y[0] = tracker_off_flag1
    y[1] = tracker_off_flag2
    y[2] = tracker_off_flag3
    y[3] = tracker_off_flag4
    y[4] = tracker_off_flag5
    y[5] = tracker_off_flag6

    return x, y
