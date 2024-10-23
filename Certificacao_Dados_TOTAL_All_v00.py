# %%

import os   
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from total_dados_entrada import total_dados_entrada
from utils import encontrar_indices, excluir_arquivos
from total_localizador import total_localizador
from total_varrad import total_varrad
#from resumo_cqd import resumo_cqd
from total_cqd_met import total_cqd_met
# Informações de entrada
arquivo = 'data/SPES01-2024-09.xlsx'

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
# Controle de qualidade de Rados Radiométricos

# [Estatistico_RAD,RAD_XLSXplot,Flags_RAD,Pot_RAD_xlsx,Energia_RAD_xlsx] = 
# TOTAL_CQD_RAD(RAW_RAD,RAW_MET,DADOS,GHI1,GHI2,GHI3,POA,GRI1,GRI2,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo,ES);
#estatistico_rad, rad_xlsxplot, flags = total_cqd_rad(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es)
total_cqd_rad(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es)

# %%
estatistico_met, met_xlsxplot, flags_met, pot_met_xlsx, blox_plot = total_cqd_met(raw_met, dados, temp, ur, press, prec, vel, dire, temp_max, temp_min, press_max, press_min, mes, dia_final, ano, 10, prec_max, nome_arquivo, es)
# %%
#resumo_cqd()
excluir_arquivos()
