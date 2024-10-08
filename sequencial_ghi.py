def sequencial_ghi(raw, dados, var_avg, var_max, var_min, var_std, ghi1_avg_p, titulo, nome_var, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo):
    n, m = raw.shape

    data = raw.iloc[:, 0].to_numpy()

    if ghi2:
        ghi2_avg = raw.iloc[:, ghi2[0]]
    if ghi3:
        ghi3_avg = raw.iloc[:, ghi3[0]]
    if poa:
        poa_avg = raw.iloc[:, poa[0]]
    if dhi:
        dhi_avg = raw.iloc[:, dhi[0]]
    if bni:
        bni_avg = raw.iloc[:, bni[0]]
    if clear_sky:
        clear_sky_avg = raw.iloc[:, clear_sky[0]]

    horalocal = dados.iloc[:,1]
    dia_mes = dados.iloc[:,2]
    cosAZS = dados.iloc[:,13]
    azs = dados.iloc[:,14]
    cosAZS12 = dados.iloc[:,15]
    alpha = dados.iloc[:,17]
    iox = dados.iloc[:,21]

    # Definição das flags
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000


    ghi1_flag1 = 0
    ghi1_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            ghi1_flag6 += 1
        else:
            ghi1_flag1 += 1    

    pass
