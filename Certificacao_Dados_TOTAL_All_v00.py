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
vetor_completo, temp, ur, press, prec, vel, dire, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, lwdn, lwup, clear_sky = total_localizador(header)


# %%
# Variáveis Radiométricas
dados = total_varrad(raw_rad, dia_juliano_ref, latitude, longitude, longitude_ref, isc, horalocal_ref, nome_arquivo)

# %%
# Controle de qualidade de Rados Radiométricos