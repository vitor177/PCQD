import pandas as pd
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
from testes.teste_kd_dhi import teste_kd_dhi
from testes.teste_tracker_off import teste_tracker_off
from flag_plot import flag_plot
from total_xplot3 import total_xplot3
import numpy as np

def sequencial_dhi(raw, dados, var_avg, var_max, var_min, var_std, var_avg_p, titulo, nome_var, ghi1, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo):
    # Informações dos dados brutos
    n, m = raw.shape

    data = raw.iloc[:, 0].to_numpy()

    if ghi1:
        ghi1_avg = raw.iloc[:, ghi1[0]]
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
        clear_sky_dhi = raw.iloc[:, clear_sky[2]]


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


    dhi_flag1 = 0
    dhi_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            dhi_flag6 += 1
        else:
            dhi_flag1 += 1    

    m1 = np.full(n, np.nan)
    m1 = var_avg
    n1 = np.full((6,1), np.nan)
    n1[0][0] = dhi_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = dhi_flag6

    nome = ["RAW"]

    print("VAR_AVG", var_avg[:5])


# [LF_DHI,LF_DHI_Flag] = TESTE_Limites_Fisicos(Var_avg,Var_avg,2000,-5,n);
# M1 = [M1,LF_DHI];
# N1 = [N1,LF_DHI_Flag];
# Nome = [Nome,{'Limites Físicos'}];

    lf_dhi, lf_dhi_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)

    m1 = np.column_stack((m1, lf_dhi))
    n1 = np.hstack((n1, lf_dhi_flag.reshape(-1,1)))
    nome.append("Limites Físicos")




    fpmin = -4
    fpmaxdhi = (0.95 * iox * cosAZS12) + 50
    ermin = -2
    ermaxdhi = (0.75 * iox * cosAZS12) + 30

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_dhi, bsnr_dhi_flag = teste_bsrn(lf_dhi, var_avg, fpmin, fpmaxdhi, ermin, ermaxdhi, n)
    #print(pd.DataFrame(n1.astype(int)))

    m1 = np.column_stack((m1, bsrn_dhi))
    n1 = np.hstack((n1, bsnr_dhi_flag))
    nome.extend(["Fisicamente Possível", "Extremamente Raro"])



# [Elevacao_DHI,Elevacao_DHI_Flag] = TESTE_angulo_elevacao(BSRN_DHI(:,2),alpha,n);
# M1 = [M1,Elevacao_DHI];
# N1 = [N1,Elevacao_DHI_Flag];
# Nome = [Nome,{'Ângulo de elevacao'}];

    elevacao_dhi, elevaco_dhi_flag = teste_angulo_elevacao(bsrn_dhi[:,1], alpha, n)

    m1 = np.column_stack((m1, elevacao_dhi))
    n1 = np.hstack((n1, elevaco_dhi_flag.reshape(-1,1)))
    nome.append("Angulo de elevação")




#     [kd_DHI,kd_DHI_Flag] = TESTE_kd_DHI(Elevacao_DHI,DHI_avg,GHI1_avg,Iox,n);
# M1 = [M1,kd_DHI(:,2)];
# N1 = [N1,kd_DHI_Flag(:,2)];
# Nome = [Nome,{'Índice de transmissividade'}];
    kd_dhi, kd_dhi_flag = teste_kd_dhi(elevacao_dhi, dhi_avg, ghi1_avg, iox, n)
    m1 = np.column_stack((m1, kd_dhi[:,1]))
    n1 = np.hstack((n1, kd_dhi_flag[:,1].reshape(-1,1)))
    nome.append("Índice de transmissividade") 



#     [std_Consistencia,std_Consistencia_flag] = TESTE_std_Consistencia(kd_DHI,Var_avg,Var_max,Var_min,Var_std,n);
# M1 = [M1,std_Consistencia];
# N1 = [N1,std_Consistencia_flag];
# Nome = [Nome,{'Desvio padrão nulo'},{'Consistência de parêmetros'}];

    std_consistencia, std_consistencia_flag = teste_std_consistencia(kd_dhi, var_avg, var_max, var_min, var_std, n)

    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    #print(pd.DataFrame(std_consistencia_flag.astype(int)))



#     [tracker,tracker_flag] = TESTE_tracker_off(std_Consistencia,GHI1_avg,DHI_avg,BNI_avg,cosAZS,AZS,Clear_sky_DHI,n);
# M1 = [M1,tracker];
# N1 = [N1,tracker_flag];
# Nome = [Nome,{'Tracker off'}];

    tracker, tracker_flag = teste_tracker_off(std_consistencia, ghi1_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_dhi, n)

    m1 = np.column_stack((m1, tracker))
    n1 = np.hstack((n1, tracker_flag.reshape(-1,1)))
    nome.append("Tracker Off") 



# [comparacao_comp,comparacao_comp_flag] = TESTE_comparacao_completo(tracker,GHI1_avg,DHI_avg,BNI_avg,cosAZS,AZS,Clear_sky_DHI,n);
# M1 = [M1,comparacao_comp(:,2)];
# N1 = [N1,comparacao_comp_flag(:,2)];
# Nome = [Nome,{'Comparacao entre variaveis DHI'}];
# Var_anterior = comparacao_comp(:,2);

    comparacao_comp, comparacao_comp_flag = teste_comparacao_completo(tracker, ghi1_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_dhi, n)
    m1 = np.column_stack((m1, comparacao_comp[:,1]))
    n1 = np.hstack((n1, comparacao_comp_flag[:,1].reshape(-1,1)))
    nome.append("Comparacao entre variaveis DHI") 
    var_anterior = comparacao_comp[:,1]

    # pegar a posição [1]

    # [consistencia,consistencia_Flag] = TESTE_consistencia(Var_anterior,Var_avg,n);
    # M1 = [M1,consistencia];
    # N1 = [N1,consistencia_Flag];
    # Nome = [Nome,{'Consistencia'}];

    consistencia, consistencia_flag = teste_consistencia(var_anterior, var_avg, n)

    m1 = np.column_stack((m1, consistencia))
    n1 = np.hstack((n1, consistencia_flag.reshape(-1,1)))
    nome.append("Consistência") 

#     [persistencia,persistencia_Flag] = TESTE_persistencia(consistencia,Var_avg_p,20,n);
# M1 = [M1,persistencia];
# N1 = [N1,persistencia_Flag];
# Nome = [Nome,{'Persistência'}];

    persistencia, persistencia_flag = teste_persistencia(consistencia, var_avg_p, 20, n)

    m1 = np.column_stack((m1, persistencia))
    n1 = np.hstack((n1, persistencia_flag.reshape(-1,1)))
    nome.append("Persistência") 

    print(pd.DataFrame(n1, columns=nome).astype(int))



# [Resultado_BNI,Resultado_Flag_BNI,Flags_BNI,Estatistico_BNI,BNI_XLSX] = Resultado_Var(persistencia,Var_avg,Nome,nome_var,data,N1,n);
# M1 = [M1,Resultado_BNI];
# N1 = [N1,Resultado_Flag_BNI];
# Nome = [Nome,{'Resultado'}];
    resultado_dhi, resultado_flag_dhi, flags_dhi, estatistico_dhi, dhi_xlsx = resultado_var(persistencia, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_dhi))
    n1 = np.hstack((n1, resultado_flag_dhi.reshape(-1,1)))

    #[Pot_DHI,Pot_DHI_xlsx] = Potencial_Var(Resultado_DHI,Var_avg,Var_max,Var_min,nome_var,horalocal,dia_mes,n);

    pot_dhi, pot_dhi_xlsx = potencial_var(resultado_dhi, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # [Energia_DHI,Energia_DHI_xlsx] = Energia_Var(Resultado_DHI,Var_avg,nome_var,n);
    energia_dhi, energia_dhi_xlsx = energia_var(resultado_dhi, var_avg, nome_var, n)

    # Flag = Flag_plot(Var_avg,Resultado_DHI);
    flag = flag_plot(var_avg, resultado_dhi)

    for i in range(n):
        if var_avg[i] > 2000:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0

    #print(flag)

    # array[~np.isnan(array)]

    


    total_xplot3(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 1000, 0, 'W/m²', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)


