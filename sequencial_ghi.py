import numpy as np
import pandas as pd
from testes.teste_limites_fisicos import teste_limites_fisicos
from testes.teste_bsrn import teste_bsrn
from testes.teste_angulo_elevacao import teste_angulo_elevacao
from testes.teste_kt_ghi import teste_kt_ghi
from testes.teste_std_consistencia import teste_std_consistencia
from testes.teste_comparacao_simples import teste_comparacao_simples
from testes.teste_comparacao_completo import teste_comparacao_completo
from testes.teste_clear_sky import teste_clear_sky
from testes.teste_consistencia import teste_consistencia
from testes.teste_persistencia import teste_persistencia


def sequencial_ghi(raw, dados, var_avg, var_max, var_min, var_std, var_avg_p, titulo, nome_var, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo):
    n, m = raw.shape

    data = raw.iloc[:, 0].to_numpy()

    clear_sky_ghi = 0

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
        clear_sky_ghi = raw.iloc[:, clear_sky[0]]

    # Informações da varRad
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

    m1 = np.full(n, np.nan)
    m1 = var_avg
    n1 = np.full(6, np.nan)
    n1[0] = ghi1_flag1
    n1[1] = 0
    n1[2] = 0
    n1[3] = 0
    n1[4] = 0
    n1[5] = ghi1_flag6

    # Nome
    lf_ghi1, lf_ghi_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)

    # TESTE BSNR
    fpmin = -4
    fpmaxghi = (1.5 * iox * cosAZS12) + 100
    ermin = -2
    ermaxghi = (1.2 * iox * cosAZS12) + 50

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_ghi1, bsnr_ghi1_flag = teste_bsrn(lf_ghi1, var_avg, fpmin, fpmaxghi, ermin, ermaxghi, n)

    #print(f"Teste aplicado BSNR: lf_ghi1: {bsrn_ghi1} e {bsnr_ghi1_flag}")

    #print("AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII: ", type(bsrn_ghi1))

    elevacao_ghi, elevacao_ghi_flag = teste_angulo_elevacao(bsrn_ghi1[:, 1], alpha, n)

    #print(f"Teste aplicado Angulo: lf_ghi1: {elevacao_ghi} e {elevacao_ghi_flag}")

    kt_ghi, kt_ghi1_flag = teste_kt_ghi(elevacao_ghi, var_avg, cosAZS, iox, n)

    #print(f"Teste aplicado KT GHI: lf_ghi1: {kt_ghi} e {kt_ghi1_flag}")

    # [std_Consistencia,std_Consistencia_flag] = TESTE_std_Consistencia(kt_GHI,Var_avg,Var_max,Var_min,Var_std,n);
    std_consistencia, std_consistencia_flag = teste_std_consistencia(kt_ghi[:, 0], var_avg, var_max, var_min, var_std, n)
    var_anterior = std_consistencia

    #print(f"Teste aplicado STD Consistencia: lf_ghi1: {std_consistencia} e {std_consistencia_flag}")

    if ghi2 and not ghi3:
        aux = []
        comparacao, comparacao_flag = teste_comparacao_simples(var_anterior, ghi2_avg, aux, n)
        var_anterior = comparacao
    if ghi2 and ghi3:
        comparacao, comparacao_flag = teste_comparacao_simples(var_anterior, ghi2_avg, aux, n)
        var_anterior = comparacao
    if dhi:
        comparacao_comp, comparacao_comp_flag  = teste_comparacao_completo(var_anterior[:,0], var_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_ghi, n)
        var_anterior = comparacao_comp
        print(comparacao_comp_flag)

    ghi_mcc_clearx = clear_sky_ghi*1.4
    ceu_claro_ghi, ceu_claro_ghi_flag = teste_clear_sky(var_anterior, var_avg, ghi_mcc_clearx, n)
    print("_--------------------------")
    print(ceu_claro_ghi, ceu_claro_ghi_flag)

    consistencia, consistencia_flag = teste_consistencia(ceu_claro_ghi, var_avg, n)

    persistencia, persistencia_flag = teste_persistencia(consistencia, var_avg_p, 20, n)
    
# %==========================================================================
# %                            GHI - Resultados
# %==========================================================================

# [Resultado_GHI1,Resultado_Flag_GHI1,Flags_GHI1,Estatistico_GHI1,GHI1_XLSX] = Resultado_Var(persistencia,Var_avg,Nome,nome_var,data,N1,n);
# M1 = [M1,Resultado_GHI1];
# N1 = [N1,Resultado_Flag_GHI1];
# Nome = [Nome,{'Resultado'}];

    #resultado_var(persistencia, var_avg, nome_arquivo, nome_var, data, n1, n)


# function [M1,N1,Nome,GHI1_XLSX,Flags_GHI1,Estatistico_GHI1,Pot_GHI1_xlsx,Energia_GHI1_xlsx] = Sequencial_GHI(RAW,DADOS,Var_avg,Var_max,Var_min,Var_std,Var_avg_p,titulo,nome_var,GHI2,GHI3,POA,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo)



    return 