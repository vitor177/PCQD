# %%


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from total_dados_entrada import total_dados_entrada
from utils import encontrar_indices
from total_localizador import total_localizador
from total_varrad import total_varrad

# Informações de entrada
arquivo = 'data/SPES01-2024-07.xlsx'

header = pd.read_excel(arquivo)
colunas = list(header.iloc[0])
colunas_cams = ['Clear Sky GHI', 'Clear Sky BHI', 'Clear Sky DHI', 'Clear Sky BNI','GHI', 'BHI', 'DHI', 'BNI']
finais = []

for i in colunas:
    if (isinstance(i, str)):
        finais.append(i)
finais.extend(colunas_cams)

header.columns = finais

raw_rad = header.iloc[1443:].reset_index(drop=True)
raw_met = header.iloc[3:].reset_index(drop=True)

# Parâmetros de entrada
longitude_ref = -45
isc = 1367
horalocal_ref = 0

# Informações das estações 
es, nome_arquivo, ano, mes, dia_juliano_ref, dia_final, latitude, longitude, altitude, temp_min, temp_max, prec_max, press_min, press_max, dfolder = total_dados_entrada(arquivo)
# %%
vetor_completo, temp, ur, press, prec, vel, dire, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, lwdn, lwup, clear_sky = total_localizador(header) # Ajeitar letra a mais


# %%
# Variáveis Radiométricas
dados = total_varrad(raw_rad, dia_juliano_ref, latitude, longitude, longitude_ref, isc, horalocal_ref, nome_arquivo) # OK
from total_cqd_rad import total_cqd_rad

# %%
def total_cqd_rad2(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es):
    #data = raw_rad.iloc[:, 0].to_numpy()


    start_row = 1440-20

    ghi1_avg = raw_rad.iloc[:, ghi1[0]]
    ghi1_max = raw_rad.iloc[:, ghi1[1]]
    ghi1_min = raw_rad.iloc[:, ghi1[2]]
    ghi1_std = raw_rad.iloc[:, ghi1[3]]
    ghi1_avg_p = raw_rad.iloc[start_row:, ghi1[0]]

    if len(ghi2) > 0:
        ghi2_avg = raw_rad.iloc[:, ghi2[0]]
        ghi2_max = raw_rad.iloc[:, ghi2[1]]
        ghi2_min = raw_rad.iloc[:, ghi2[2]]
        ghi2_std = raw_rad.iloc[:, ghi2[3]]
        ghi2_avg_p = raw_rad.iloc[start_row:, ghi2[0]]

    if len(ghi3) > 0:
        ghi3_avg = raw_rad.iloc[:, ghi3[0]]
        ghi3_max = raw_rad.iloc[:, ghi3[1]]
        ghi3_min = raw_rad.iloc[:, ghi3[2]]
        ghi3_std = raw_rad.iloc[:, ghi3[3]]
        ghi3_avg_p = raw_rad.iloc[start_row:, ghi3[0]]

    if len(poa) > 0:
        poa_avg = raw_rad.iloc[:, poa[0]]
        poa_max = raw_rad.iloc[:, poa[1]]
        poa_min = raw_rad.iloc[:, poa[2]]
        poa_std = raw_rad.iloc[:, poa[3]]
        poa_avg_p = raw_rad.iloc[start_row:, poa[0]]

    if len(dhi) > 0:
        dhi_avg = raw_rad.iloc[:, dhi[0]]
        dhi_max = raw_rad.iloc[:, dhi[1]]
        dhi_min = raw_rad.iloc[:, dhi[2]]
        dhi_std = raw_rad.iloc[:, dhi[3]]
        dhi_avg_p = raw_rad.iloc[start_row:, dhi[0]]

    if len(bni) > 0:
        bni_avg = raw_rad.iloc[:, bni[0]]
        bni_max = raw_rad.iloc[:, bni[1]]
        bni_min = raw_rad.iloc[:, bni[2]]
        bni_std = raw_rad.iloc[:, bni[3]]
        bni_avg_p = raw_rad.iloc[start_row:, bni[0]]

    if len(gri1) > 0:
        gri1_avg = raw_rad.iloc[:, gri1[0]]
        gri1_max = raw_rad.iloc[:, gri1[1]]
        gri1_min = raw_rad.iloc[:, gri1[2]]
        gri1_std = raw_rad.iloc[:, gri1[3]]
        gri1_avg_p = raw_rad.iloc[start_row:, gri1[0]]

    if len(gri2) > 0:
        gri2_avg = raw_rad.iloc[:, gri2[0]]
        gri2_max = raw_rad.iloc[:, gri2[1]]
        gri2_min = raw_rad.iloc[:, gri2[2]]
        gri2_std = raw_rad.iloc[:, gri2[3]]
        gri2_avg_p = raw_rad.iloc[start_row:, gri2[0]]

    if len(clear_sky) > 0:
        clear_sky_avg = raw_rad.iloc[:, clear_sky[0]]
        clear_sky_max = raw_rad.iloc[:, clear_sky[1]]
        clear_sky_min = raw_rad.iloc[:, clear_sky[2]]
        clear_sky_std = raw_rad.iloc[:, clear_sky[3]]
        clear_sky_avg_p = raw_rad.iloc[start_row:, clear_sky[0]]

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
    if not ghi2:
# [GHI_M1,GHI_N1,GHI_Nome,GHI_XLSX,Flags_GHI,Estatistico_GHI,Pot_GHI_xlsx,Energia_GHI_xlsx] = Sequencial_GHI(RAW_RAD,DADOS,GHI1_avg,GHI1_max,GHI1_min,GHI1_std,GHI1_avg_p,'Global Horizontal Irradiance ','GHI',GHI2,GHI3,POA,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo);
        ghi_m1, ghi_n1, ghi_nome, ghi_xlsx, flags_ghi, estatistico_ghi, pot_ghi_xlsx, energia_ghi_xlsx = sequencial_ghi(raw_rad, dados, ghi1_avg, ghi1_max, ghi1_min, ghi1_std, ghi1_avg_p, 'Global Horizontal Irradiance ', 'GHI', ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)


    return ghi1_avg, ghi1_max, ghi1_avg_p
# Controle de qualidade de Rados Radiométricos

# [Estatistico_RAD,RAD_XLSXplot,Flags_RAD,Pot_RAD_xlsx,Energia_RAD_xlsx] = 
# TOTAL_CQD_RAD(RAW_RAD,RAW_MET,DADOS,GHI1,GHI2,GHI3,POA,GRI1,GRI2,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo,ES);
#estatistico_rad, rad_xlsxplot, flags = total_cqd_rad(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es)
receba = total_cqd_rad2(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es)

# %%
type(c)
# %%
b
# %%
