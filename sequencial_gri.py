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
from testes.teste_tracker_off import teste_tracker_off
from testes.teste_kn_bni import teste_kn_bni
from flag_plot import flag_plot
from total_xplot3c import total_xplot3c
from total_xplot3 import total_xplot3
import numpy as np
# function [M1,N1,Nome,GRI_XLSX,Flags_GRI,Estatistico_GRI,Pot_GRI_xlsx,Energia_GRI_xlsx] = Sequencial_GRI(RAW,DADOS,Var_avg,Var_max,Var_min,Var_std,Var_avg_p,titulo,nome_var,GRI2,Clear_sky,mes,dia_final,ano,Nome_Arquivo)
def sequencial_gri(raw, dados, var_avg, var_max, var_min, var_std, var_avg_p, titulo, nome_var, gri2, clear_sky, mes, dia_final, ano, nome_arquivo):
    # Informações dos dados brutos

    albedo_max = 0.3

    n, m = raw.shape

    data = raw.iloc[:, 0].to_numpy()

    if gri2:
        gri2_avg = raw.iloc[:, gri2[0]]
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


    gri_flag1 = 0
    gri_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            gri_flag6 += 1
        else:
            gri_flag1 += 1    

    m1 = np.full(n, np.nan)
    m1 = var_avg
    n1 = np.full((6,1), np.nan)
    n1[0][0] = gri_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = gri_flag6

    nome = ["RAW"]

    lf_gri, lf_gri_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)
    m1 = np.column_stack((m1, lf_gri))
    n1 = np.hstack((n1, lf_gri_flag.reshape(-1,1)))
    nome.append("Limites Físicos")


    fpmin = -4
    fpmaxgri = ((1.5*iox*cosAZS12)+100)*albedo_max
    ermin = -2
    ermaxgri = ((1.2*iox*cosAZS12)+50)*albedo_max

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_gri, bsnr_gri_flag = teste_bsrn(lf_gri, var_avg, fpmin, fpmaxgri, ermin, ermaxgri, n)
    m1 = np.column_stack((m1, bsrn_gri))
    n1 = np.hstack((n1, bsnr_gri_flag))
    nome.extend(["Fisicamente Possível", "Extremamente Raro"])

    elevacao_gri, elevaco_gri_flag = teste_angulo_elevacao(bsrn_gri[:,1], alpha, n)
    m1 = np.column_stack((m1, elevacao_gri))
    n1 = np.hstack((n1, elevaco_gri_flag.reshape(-1,1)))
    nome.append("Angulo de elevação")


    std_consistencia, std_consistencia_flag = teste_std_consistencia(elevacao_gri, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])
    var_anterior = std_consistencia

    # Comparação entre sensores

    aux = []
    if gri2:
        comparacao, comparacao_flag = teste_comparacao_simples(var_anterior, gri2_avg, aux, n)
        m1 = np.column_stack((m1, comparacao))
        n1 = np.hstack((n1, comparacao_flag.reshape(-1,1)))
        nome.append("Comparação entre sensores")
        var_anterior = comparacao

    gri_mcc_clearx = (clear_sky_ghi*1.4)*albedo_max

    ceu_claro_gri, ceu_claro_gri_flag = teste_clear_sky(var_anterior, var_avg, gri_mcc_clearx, n)
    m1 = np.column_stack((m1, ceu_claro_gri))
    n1 = np.hstack((n1, ceu_claro_gri_flag.reshape(-1,1)))
    nome.append("Céu Claro") 
    

    consistencia, consistencia_flag = teste_consistencia(ceu_claro_gri, var_avg, n)
    m1 = np.column_stack((m1, consistencia))
    n1 = np.hstack((n1, consistencia_flag.reshape(-1,1)))
    nome.append("Consistência") 

    persistencia, persistencia_flag = teste_persistencia(consistencia, var_avg_p, 20, n)
    m1 = np.column_stack((m1, persistencia))
    n1 = np.hstack((n1, persistencia_flag.reshape(-1,1)))
    nome.append("Persistência") 

    resultado_gri, resultado_flag_gri, flags_gri, estatistico_gri, gri_xlsx = resultado_var(persistencia, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_gri))
    n1 = np.hstack((n1, resultado_flag_gri.reshape(-1,1)))

    pot_gri, pot_gri_xlsx = potencial_var(resultado_gri, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # [Energia_DHI,Energia_DHI_xlsx] = Energia_Var(Resultado_DHI,Var_avg,nome_var,n);
    energia_gri, energia_gri_xlsx = energia_var(resultado_gri, var_avg, nome_var, n)

    # Flag = Flag_plot(Var_avg,Resultado_DHI);
    flag = flag_plot(var_avg, resultado_gri)

    for i in range(n):
        if var_avg[i] > 2000:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0



    total_xplot3(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 1800*albedo_max, 0, 'W/m²', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)

    total_xplot3c(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 1800*albedo_max, 0, 'W/m²', 10,'BNI max','BNI min', 'BNI avg', nome_arquivo)
    

    return m1, n1.T, nome, gri_xlsx, pd.DataFrame(flags_gri.T), pd.DataFrame(estatistico_gri), pot_gri_xlsx, energia_gri_xlsx