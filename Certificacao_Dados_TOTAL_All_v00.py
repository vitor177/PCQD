# %%


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from total_dados_entrada import total_dados_entrada
from utils import encontrar_indices

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

longitude_ref = -45
isc = 1367
horalocal_ref = 0


es, nome_arquivo, ano, mes, dia_juliano_ref, dia_final, latitude, longitude, altitude, temp_min, temp_max, prec_max, press_min, press_max, dfolder = total_dados_entrada(arquivo)
# %%
vetor = header.iloc[0:3].values.flatten()
vetor_minusculo = [str(valor).lower() for valor in vetor if isinstance(valor, str)]

print(vetor_minusculo)
# %%
vetor_completo = pd.DataFrame()
vetor_completo


# %%
# %%
col_temp = ["Temp_avg","Temp_max", "Temp_min", "Temp_std"]


temp = encontrar_indices(col_temp, finais)
temp
# %%
for i, item in enumerate(finais):
    print(i, item)
# %%
