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
        clear_sky_dhi = raw.iloc[:, clear_sky[0]]


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



# [LF_DHI,LF_DHI_Flag] = TESTE_Limites_Fisicos(Var_avg,Var_avg,2000,-5,n);
# M1 = [M1,LF_DHI];
# N1 = [N1,LF_DHI_Flag];
# Nome = [Nome,{'Limites Físicos'}];

    lf_dhi, lf_dhi_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)



    fpmin = -4
    fpmaxdhi = (0.95 * iox * cosAZS12) + 50
    ermin = -2
    ermaxdhi = (0.75 * iox * cosAZS12) + 30

    #print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
    bsrn_dhi, bsnr_dhi_flag = teste_bsrn(lf_dhi, var_avg, fpmin, fpmaxdhi, ermin, ermaxdhi, n)
    #print(pd.DataFrame(n1.astype(int)))
    print(pd.DataFrame(bsnr_dhi_flag.astype(int)))

