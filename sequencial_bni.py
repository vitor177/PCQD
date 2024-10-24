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

def sequencial_bni(raw, dados, var_avg, var_max, var_min, var_std, var_avg_p, titulo, nome_var, ghi1, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo):
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
        clear_sky_bni = raw.iloc[:, clear_sky[3]]


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


    bni_flag1 = 0
    bni_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            bni_flag6 += 1
        else:
            bni_flag1 += 1    

    m1 = np.full(n, np.nan)
    m1 = var_avg
    n1 = np.full((6,1), np.nan)
    n1[0][0] = bni_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = bni_flag6

    nome = ["RAW"]

    lf_bni, lf_bni_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)
    m1 = np.column_stack((m1, lf_bni))
    n1 = np.hstack((n1, lf_bni_flag.reshape(-1,1)))
    nome.append("Limites Físicos")




    fpmin = -4
    fpmaxbni = iox
    ermin = -2
    ermaxbni = (0.95 * iox * cosAZS12) + 10

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_bni, bsnr_bni_flag = teste_bsrn(lf_bni, var_avg, fpmin, fpmaxbni, ermin, ermaxbni, n)
    #print(pd.DataFrame(n1.astype(int)))

    m1 = np.column_stack((m1, bsrn_bni))
    n1 = np.hstack((n1, bsnr_bni_flag))
    nome.extend(["Fisicamente Possível", "Extremamente Raro"])

    elevacao_bni, elevaco_bni_flag = teste_angulo_elevacao(bsrn_bni[:,1], alpha, n)

    m1 = np.column_stack((m1, elevacao_bni))
    n1 = np.hstack((n1, elevaco_bni_flag.reshape(-1,1)))
    nome.append("Angulo de elevação")

    # Escrever o teste_kn_bni
    kn_bni, kn_bni_flag = teste_kn_bni(elevacao_bni, var_avg, iox, n)
    m1 = np.column_stack((m1, kn_bni[:,1]))
    n1 = np.hstack((n1, kn_bni_flag[:,1].reshape(-1,1)))
    nome.append("Índice de transmissividade") 



    std_consistencia, std_consistencia_flag = teste_std_consistencia(kn_bni, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    tracker, tracker_flag = teste_tracker_off(std_consistencia, ghi1_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_bni, n)
    m1 = np.column_stack((m1, tracker))
    n1 = np.hstack((n1, tracker_flag.reshape(-1,1)))
    nome.append("Tracker Off") 

    comparacao_comp, comparacao_comp_flag = teste_comparacao_completo(tracker, ghi1_avg, dhi_avg, bni_avg, cosAZS, azs, clear_sky_bni, n)
    m1 = np.column_stack((m1, comparacao_comp[:,2]))
    n1 = np.hstack((n1, comparacao_comp_flag[:,2].reshape(-1,1)))
    nome.append("Comparacao entre variaveis BNI") 
    var_anterior = comparacao_comp[:,2]



    bni_mcc_clearx = clear_sky_bni*1.1
    ceu_claro_bni, ceu_claro_bni_flag = teste_clear_sky(var_anterior, var_avg, bni_mcc_clearx, n)
    m1 = np.column_stack((m1, ceu_claro_bni))
    n1 = np.hstack((n1, ceu_claro_bni_flag.reshape(-1,1)))
    nome.append("Céu Claro") 

    consistencia, consistencia_flag = teste_consistencia(ceu_claro_bni, var_avg, n)
    m1 = np.column_stack((m1, consistencia))
    n1 = np.hstack((n1, consistencia_flag.reshape(-1,1)))
    nome.append("Consistência") 

    persistencia, persistencia_flag = teste_persistencia(consistencia, var_avg_p, 20, n)
    m1 = np.column_stack((m1, persistencia))
    n1 = np.hstack((n1, persistencia_flag.reshape(-1,1)))
    nome.append("Persistência") 

    print(pd.DataFrame(n1, columns=nome).astype(int))

    resultado_bni, resultado_flag_bni, flags_bni, estatistico_bni, bni_xlsx = resultado_var(persistencia, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_bni))
    n1 = np.hstack((n1, resultado_flag_bni.reshape(-1,1)))


    pot_bni, pot_bni_xlsx = potencial_var(resultado_bni, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # [Energia_DHI,Energia_DHI_xlsx] = Energia_Var(Resultado_DHI,Var_avg,nome_var,n);
    energia_bni, energia_bni_xlsx = energia_var(resultado_bni, var_avg, nome_var, n)

    # Flag = Flag_plot(Var_avg,Resultado_DHI);
    flag = flag_plot(var_avg, resultado_bni)

    for i in range(n):
        if var_avg[i] > 2000:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0



    total_xplot3(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 1400, 0, 'W/m²', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)


    # TOTAL_Xplot3C(Var_max,Var_min,Var_avg,data,2,titulo,dia_final,mes,ano,1000,0,'W/m²',10,'DHI max','DHI min','DHI avg',Nome_Arquivo)


    total_xplot3c(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 1400, 0, 'W/m²', 10,'BNI max','BNI min', 'BNI avg', nome_arquivo)
    
    
    return m1, n1, nome, bni_xlsx, pd.DataFrame(flags_bni.T), pd.DataFrame(estatistico_bni), pot_bni_xlsx, energia_bni_xlsx
        # total_xplot3c(variavel1=ghi_max,
        #         variavel2=ghi_min,
        #         variavel3=ghi_avg,
        #         data=data,
        #         num_figura=fig+2,
        #         titulo=titulo,
        #         diafinal=dia_final,
        #         mes=mes,
        #         ano=anox,
        #         lim_sy=1800,
        #         lim_iy=0,
        #         und_y='[m/s]',
        #         tam_font=10,
        #         var1='GHI1 max',
        #         var2='GHI12 min',
        #         var3='GHI1 avg',
        #         nome_arquivo=nome_arquivo)