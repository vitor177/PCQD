import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from total_dados_entrada import total_dados_entrada

arquivo = 'data/SPES01-2024-07.xlsx'

es, nome_arquivo, ano, mes, dia_juliano_ref, dia_final, latitude, longitude, altitude, temp_min, temp_max, prec_max, press_min, press_max, dfolder = total_dados_entrada(arquivo)

print(dfolder)
