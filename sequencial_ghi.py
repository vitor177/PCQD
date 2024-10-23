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
from resultado_var import resultado_var
from potencial_var import potencial_var
from energia_var import energia_var

def sequencial_ghi(raw, dados, var_avg, var_max, var_min, var_std, var_avg_p, titulo, nome_var, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo):
    n, m = raw.shape

    data = raw.iloc[:, 0].to_numpy()

    clear_sky_ghi = np.zeros(n)

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
    n1 = np.full((6,1), np.nan)
    n1[0][0] = ghi1_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = ghi1_flag6

    nome = ["RAW"]

    # Nome
    lf_ghi1, lf_ghi_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)

    m1 = np.column_stack((m1, lf_ghi1))
    n1 = np.hstack((n1, lf_ghi_flag.reshape(-1,1)))
    nome.append("Limites Físicos")

    fpmin = -4
    fpmaxghi = (1.5 * iox * cosAZS12) + 100
    ermin = -2
    ermaxghi = (1.2 * iox * cosAZS12) + 50

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_ghi1, bsnr_ghi1_flag = teste_bsrn(lf_ghi1, var_avg, fpmin, fpmaxghi, ermin, ermaxghi, n)
    m1 = np.column_stack((m1, bsrn_ghi1))
    n1 = np.hstack((n1, bsnr_ghi1_flag))
    nome.extend(["Fisicamente Possível", "Extremamente Raro"])

    elevacao_ghi, elevacao_ghi_flag = teste_angulo_elevacao(bsrn_ghi1[:, 0], alpha, n)
    m1 = np.column_stack((m1, elevacao_ghi))
    n1 = np.hstack((n1, elevacao_ghi_flag.reshape(-1,1)))
    nome.append("Angulo de elevação")

    kt_ghi, kt_ghi1_flag = teste_kt_ghi(elevacao_ghi, var_avg, cosAZS, iox, n)
    m1 = np.column_stack((m1, kt_ghi[:,1]))
    n1 = np.hstack((n1, kt_ghi1_flag[:,1].reshape(-1,1)))
    nome.append("Índice de transmissividade")

    std_consistencia, std_consistencia_flag = teste_std_consistencia(kt_ghi[:, 0], var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    var_anterior = std_consistencia

    if ghi2 and not ghi3:
        aux = []
        comparacao, comparacao_flag = teste_comparacao_simples(var_anterior, ghi2_avg, aux, n)
        m1 = np.column_stack((m1, comparacao))
        n1 = np.hstack((n1, comparacao_flag.reshape(-1,1)))
        nome.append("Comparação entre sensores")
        
        var_anterior = comparacao
    if ghi2 and ghi3:
        comparacao, comparacao_flag = teste_comparacao_simples(var_anterior, ghi2_avg, aux, n)
        m1 = np.column_stack((m1, comparacao))
        n1 = np.hstack((n1, comparacao_flag.reshape(-1,1)))
        nome.append("Comparação entre sensores")
        var_anterior = comparacao
    if dhi:
        comparacao_comp, comparacao_comp_flag  = teste_comparacao_completo(var_anterior[:,0], var_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_ghi, n)
        m1 = np.column_stack((m1, comparacao_comp[:n]))
        n1 = np.hstack((n1, comparacao_comp_flag[:,0].reshape(-1,1)))
        nome.append("Comparacao entre variaveis GHI")
        var_anterior = comparacao_comp


    ghi_mcc_clearx = clear_sky_ghi*1.4
    ceu_claro_ghi, ceu_claro_ghi_flag = teste_clear_sky(var_anterior, var_avg, ghi_mcc_clearx, n)
    m1 = np.column_stack((m1, ceu_claro_ghi))
    n1 = np.hstack((n1, ceu_claro_ghi_flag.reshape(-1,1)))
    nome.append("Céu Claro")
    
    consistencia, consistencia_flag = teste_consistencia(ceu_claro_ghi, var_avg, n)
    m1 = np.column_stack((m1, consistencia))
    n1 = np.hstack((n1, consistencia_flag.reshape(-1,1)))
    nome.append("Consistência")

    persistencia, persistencia_flag = teste_persistencia(consistencia, var_avg_p, 20, n)
    m1 = np.column_stack((m1, persistencia))
    n1 = np.hstack((n1, persistencia_flag.reshape(-1,1)))
    nome.append("Persistência")






    # %======= Consolidação dos resultados ======
    resultado_ghi1, resultado_flag_ghi1, flags_ghi1, estatistico_ghi1, ghi1_xlsx =  resultado_var(persistencia, var_avg, nome, nome_var, data, n1, n)


# % ======= Calculo do Potêncial =========
# [Pot_GHI1,Pot_GHI1_xlsx] = Potencial_Var(Resultado_GHI1,Var_avg,Var_max,Var_min,nome_var,horalocal,dia_mes,n);
    #pot_ghi1, pot_ghi1xlsx = potencial_var(resultado_ghi1, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    #print(pot_ghi1xlsx)

    # Cálculo da Energia
    # [Energia_GHI1,Energia_GHI1_xlsx] = Energia_Var(Resultado_GHI1,Var_avg,nome_var,n);
    #energia_ghi1, energia_ghi1_xlsx = energia_var(resultado_ghi1, var_avg, nome_var, n)

    #print(energia_ghi1)
    
    
# %==========================================================================
# %                            GHI - Resultados
# %==========================================================================

# [Resultado_GHI1,Resultado_Flag_GHI1,Flags_GHI1,Estatistico_GHI1,GHI1_XLSX] = Resultado_Var(persistencia,Var_avg,Nome,nome_var,data,N1,n);
# M1 = [M1,Resultado_GHI1];
# N1 = [N1,Resultado_Flag_GHI1];
# Nome = [Nome,{'Resultado'}];

    #resultado_var(persistencia, var_avg, nome_arquivo, nome_var, data, n1, n)

    return 