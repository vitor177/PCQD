import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from total_dados_entrada import total_dados_entrada

arquivo = 'data/SPES01-2024-07.xlsx'

header = pd.read_excel(arquivo)
raw_rad = header.iloc[1443:].reset_index(drop=True)
raw_met = header.iloc[3:].reset_index(drop=True)

longitude_ref = -45
isc = 1367
horalocal_ref = 0


es, nome_arquivo, ano, mes, dia_juliano_ref, dia_final, latitude, longitude, altitude, temp_min, temp_max, prec_max, press_min, press_max, dfolder = total_dados_entrada(arquivo)




# [Vetor_completo,TEMP,UR,PRESS,PREC,VEL,DIR,GHI1,GHI2,GHI3,POA,GRI1,GRI2,DHI,BNI,LWdn,LWup,Clear_sky] = TOTAL_Localizador(header);

# %==========================================================================
# %                      Variáveis Radiométricas    
# %==========================================================================

# DADOS = TOTAL_VarRAD(RAW_RAD,Dia_juliano_ref,Latitude,Longitude,Longitude_ref,Altitude,Isc,horalocal_ref,Nome_Arquivo);

# % ==========================================================================
# %                Controle de qualidade de dados Radiométricos  
# % ==========================================================================

# [Estatistico_RAD,RAD_XLSXplot,Flags_RAD,Pot_RAD_xlsx,Energia_RAD_xlsx] = TOTAL_CQD_RAD(RAW_RAD,RAW_MET,DADOS,GHI1,GHI2,GHI3,POA,GRI1,GRI2,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo,ES);

# % ==========================================================================
# %               Controle de qualidade de dados Meteorologicos  
# % ==========================================================================

# [Estatistico_MET,MET_XLSXplot,Flags_MET,Pot_MET_xlsx,Blox_plot] = TOTAL_CQD_MET(RAW_MET,DADOS,TEMP,UR,PRESS,PREC,VEL,DIR,Temp_max,Temp_min,Press_max,Press_min,mes,dia_final,ano,10,prec_max,Nome_Arquivo,ES);

# % ==========================================================================
# %               Finalização do controle de qualidade  
# % ==========================================================================

# Resumo_CQD(Estatistico_RAD,Estatistico_MET,RAD_XLSXplot,MET_XLSXplot,Flags_RAD,Flags_MET,Pot_RAD_xlsx,Pot_MET_xlsx,Nome_Arquivo);
# %%
vetor = header.iloc[0:3].values.flatten()

vetor_minusculo = [str(valor).lower() for valor in vetor if isinstance(valor, str)]

print(vetor_minusculo)

# %%
