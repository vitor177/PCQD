import pandas as pd
import numpy as np
from sequencial_ghi import sequencial_ghi
from sequencial_dhi import sequencial_dhi
from sequencial_bni import sequencial_bni
from sequencial_gri import sequencial_gri
from sequencial_ur import sequencial_ur
from sequencial_temp import sequencial_temp
# from sequencial_ur import sequencial_ur
from sequencial_vel import sequencial_vel
from sequencial_dire import sequencial_dire
from sequencial_press import sequencial_press
#from sequencial_prec import sequencial_prec

from total_over_irradiance import total_over_irradiance
def total_cqd_met(raw, dados, temp, ur, press, prec, vel, dire, temp_fp_max, temp_fp_min, lims_press, limi_press, mes, dia_final, ano, fig, prec_max, nome_arquivo, es):
    n, m = raw.shape
    dia_anterior = 1440

    data = raw.iloc[dia_anterior:, 0]

    dia_mes = dados.iloc[:, 2]

    if temp:
        temp_avg = raw.iloc[dia_anterior:, temp[0]].to_numpy()
        temp_max = raw.iloc[dia_anterior:, temp[1]].to_numpy()
        temp_min = raw.iloc[dia_anterior:, temp[2]].to_numpy()
        temp_std = raw.iloc[dia_anterior:, temp[3]].to_numpy()
        temp_avg_dia = raw.iloc[:, temp[0]].to_numpy()    

    if ur:
        ur_avg = raw.iloc[dia_anterior:, ur[0]].to_numpy()
        ur_max = raw.iloc[dia_anterior:, ur[1]].to_numpy()
        ur_min = raw.iloc[dia_anterior:, ur[2]].to_numpy()
        ur_std = raw.iloc[dia_anterior:, ur[3]].to_numpy()
        ur_avg_dia = raw.iloc[:, ur[0]].to_numpy()  
        if es == 'SPES01':
            ur_avg = (raw.iloc[dia_anterior:, ur[0]] * 100).to_numpy()  # Multiplicando e convertendo
            ur_max = (raw.iloc[dia_anterior:, ur[1]] * 100).to_numpy()  # Multiplicando e convertendo
            ur_min = (raw.iloc[dia_anterior:, ur[2]] * 100).to_numpy()  # Multiplicando e convertendo
            ur_std = (raw.iloc[dia_anterior:, ur[3]] * 100).to_numpy()  # Multiplicando e convertendo
            ur_avg_dia = (raw.iloc[:, ur[0]] * 100).to_numpy()
    if press:
        press_avg = raw.iloc[dia_anterior:, press[0]].to_numpy()
        press_max = raw.iloc[dia_anterior:, press[1]].to_numpy()
        press_min = raw.iloc[dia_anterior:, press[2]].to_numpy()
        press_std = raw.iloc[dia_anterior:, press[3]].to_numpy()
        press_avg_dia = raw.iloc[:, press[0]].to_numpy()  

    if prec:
        prec_avg = raw.iloc[dia_anterior:, prec[0]].to_numpy()
        prec_avg_dia = raw.iloc[:, prec[0]].to_numpy() 



    
    if vel:
        vel_avg = raw.iloc[dia_anterior:, vel[0]].to_numpy()
        vel_max = raw.iloc[dia_anterior:, vel[1]].to_numpy()
        vel_min = raw.iloc[dia_anterior:, vel[2]].to_numpy()
        vel_std = raw.iloc[dia_anterior:, vel[3]].to_numpy()
        vel_avg_dia = raw.iloc[:, vel[0]].to_numpy()
    if dire:
        dire_avg = raw.iloc[dia_anterior:, dire[0]].to_numpy()
        dire_max = raw.iloc[dia_anterior:, dire[1]].to_numpy()
        dire_min = raw.iloc[dia_anterior:, dire[2]].to_numpy()
        dire_std = raw.iloc[dia_anterior:, dire[3]].to_numpy()
        dire_avg_dia = raw.iloc[:, dire[0]]

    horalocal = dados.iloc[:, 1]
    dia_mes = dados.iloc[:, 2]

    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000  

    if temp:
        sequencial_temp(raw, temp_avg, temp_max, temp_min, temp_std, temp_avg_dia, temp_fp_min, temp_fp_min, 'Air temperature ','Temp', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_TEMP
        pass
    if ur:
        sequencial_ur(raw, ur_avg, ur_max, ur_min, ur_std, ur_avg_dia, 'Relative Humidity of the Air ', 'RH', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_UR
        pass
    if vel:
        sequencial_vel(raw, vel_avg, vel_max, vel_min, vel_std, vel_avg_dia, 'Wind Speed ', 'WS', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_VEL
        pass
    if dire:
        sequencial_dire(raw, dire_avg, dire_max, dire_min, dire_std, dire_avg_dia, 'Wind Direction ', 'WD', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_DIR
        pass
    if press:
        sequencial_press(raw, press_avg, press_max, press_min, press_std, press_avg_dia, lims_press, limi_press, 'Pressure', 'P', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo, es)
        # Sequencial_PRESS
        pass
    if prec:
        #sequencial_prec()
        # Sequencial_PREC

        pass


    return 