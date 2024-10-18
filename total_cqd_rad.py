import pandas as pd
import numpy as np
from sequencial_ghi import sequencial_ghi
from sequencial_dhi import sequencial_dhi
def total_cqd_rad(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es):
    data = raw_rad.iloc[:, 0].to_numpy()

    start_row = 1440-20

    ghi1_avg = raw_rad.iloc[:, ghi1[0]]

    ghi1_max = raw_rad.iloc[:, ghi1[1]]
    ghi1_min = raw_rad.iloc[:, ghi1[2]]
    ghi1_std = raw_rad.iloc[:, ghi1[3]]
    ghi1_avg_p = raw_met.iloc[start_row:, ghi1[0]]

    if len(ghi2) > 0:
        ghi2_avg = raw_rad.iloc[:, ghi2[0]]
        ghi2_max = raw_rad.iloc[:, ghi2[1]]
        ghi2_min = raw_rad.iloc[:, ghi2[2]]
        ghi2_std = raw_rad.iloc[:, ghi2[3]]
        ghi2_avg_p = raw_met.iloc[start_row:, ghi2[0]]

    if len(ghi3) > 0:
        ghi3_avg = raw_rad.iloc[:, ghi3[0]]
        ghi3_max = raw_rad.iloc[:, ghi3[1]]
        ghi3_min = raw_rad.iloc[:, ghi3[2]]
        ghi3_std = raw_rad.iloc[:, ghi3[3]]
        ghi3_avg_p = raw_met.iloc[start_row:, ghi3[0]]

    if len(poa) > 0:
        poa_avg = raw_rad.iloc[:, poa[0]]
        poa_max = raw_rad.iloc[:, poa[1]]
        poa_min = raw_rad.iloc[:, poa[2]]
        poa_std = raw_rad.iloc[:, poa[3]]
        poa_avg_p = raw_met.iloc[start_row:, poa[0]]

    if len(dhi) > 0:
        dhi_avg = raw_rad.iloc[:, dhi[0]]
        dhi_max = raw_rad.iloc[:, dhi[1]]
        dhi_min = raw_rad.iloc[:, dhi[2]]
        dhi_std = raw_rad.iloc[:, dhi[3]]
        dhi_avg_p = raw_met.iloc[start_row:, dhi[0]]

        #print("DHIAVGGGGGGGGGGGGGGGGG: ", dhi_avg[:5])

    if len(bni) > 0:
        bni_avg = raw_rad.iloc[:, bni[0]]
        bni_max = raw_rad.iloc[:, bni[1]]
        bni_min = raw_rad.iloc[:, bni[2]]
        bni_std = raw_rad.iloc[:, bni[3]]
        bni_avg_p = raw_met.iloc[start_row:, bni[0]]

    if len(gri1) > 0:
        gri1_avg = raw_rad.iloc[:, gri1[0]]
        gri1_max = raw_rad.iloc[:, gri1[1]]
        gri1_min = raw_rad.iloc[:, gri1[2]]
        gri1_std = raw_rad.iloc[:, gri1[3]]
        gri1_avg_p = raw_met.iloc[start_row:, gri1[0]]

    if len(gri2) > 0:
        gri2_avg = raw_rad.iloc[:, gri2[0]]
        gri2_max = raw_rad.iloc[:, gri2[1]]
        gri2_min = raw_rad.iloc[:, gri2[2]]
        gri2_std = raw_rad.iloc[:, gri2[3]]
        gri2_avg_p = raw_met.iloc[start_row:, gri2[0]]

    if len(clear_sky) > 0:
        clear_sky_ghi = raw_rad.iloc[:, clear_sky[0]]
        clear_sky_bhi = raw_rad.iloc[:, clear_sky[1]]
        clear_sky_dhi = raw_rad.iloc[:, clear_sky[2]]
        clear_sky_bni = raw_rad.iloc[:, clear_sky[3]]
        ghi_cams = raw_rad.iloc[:, clear_sky[4]]
        bhi_cams = raw_rad.iloc[:, clear_sky[5]]
        dhi_cams = raw_rad.iloc[:, clear_sky[6]]
        bni_cams = raw_rad.iloc[:, clear_sky[7]]


    n, m = raw_rad.shape

    horalocal = dados.iloc[:,1]
    dia_mes = dados.iloc[:,2]
    cosAZS = dados.iloc[:,13]
    azs = dados.iloc[:,14]
    cosAZS12 = dados.iloc[:,15]
    alpha = dados.iloc[:,17]
    ioh = dados.iloc[:,19]
    iox = dados.iloc[:,21]

# %return
# if isempty(GHI2)    
# [GHI_M1,GHI_N1,GHI_Nome,GHI_XLSX,Flags_GHI,Estatistico_GHI,Pot_GHI_xlsx,Energia_GHI_xlsx] = Sequencial_GHI(RAW_RAD,DADOS,GHI1_avg,GHI1_max,GHI1_min,GHI1_std,GHI1_avg_p,'Global Horizontal Irradiance ','GHI',GHI2,GHI3,POA,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo);
# [GHI_Over] = TOTAL_Over_Irradiance(RAW_RAD,DADOS,GHI1,Clear_sky,dia_final,mes,ano,'Overirradiance Events - GHI ','GHI',Nome_Arquivo);
# end


    # TO AQUI

    # is empty ghi2
    if not ghi2:
        #sequencial_ghi(raw_rad, dados, ghi1_avg, ghi1_max, ghi1_min, ghi1_std, ghi1_avg_p, 'Global Horizontal Irradiance ', 'GHI', ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        pass
    if dhi:
        sequencial_dhi(raw_rad, dados, dhi_avg, dhi_max, dhi_min, dhi_std, dhi_avg_p, 'Diffuse Horizontal Irradiance ', 'DHI', ghi1, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
   

    return 