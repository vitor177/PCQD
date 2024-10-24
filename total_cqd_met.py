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
from sequencial_prec import sequencial_prec

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
        temp_m1, temp_n1, temp_nome, temp_xlsx, flags_temp, estatistico_temp, pot_temp_xlsx, blox_plot_temp = sequencial_temp(raw, temp_avg, temp_max, temp_min, temp_std, temp_avg_dia, temp_fp_min, temp_fp_min, 'Air temperature ','Temp', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_TEMP
    if ur:
        ur_m1, ur_n1, ur_nome, ur_xlsx, flags_ur, estatistico_ur, pot_ur_xlsx, blox_plot_ur = sequencial_ur(raw, ur_avg, ur_max, ur_min, ur_std, ur_avg_dia, 'Relative Humidity of the Air ', 'RH', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_UR
    if vel:
        vel_m1, vel_n1, vel_nome, vel_xlsx, flags_vel, estatistico_vel, pot_vel_xlsx, blox_plot_vel = sequencial_vel(raw, vel_avg, vel_max, vel_min, vel_std, vel_avg_dia, 'Wind Speed ', 'WS', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_VEL
    if dire:
        dire_m1, dire_n1, dire_nome, dire_xlsx, flags_dire, estatistico_dire, pot_dire_xlsx, blox_plot_dire = sequencial_dire(raw, dire_avg, dire_max, dire_min, dire_std, dire_avg_dia, 'Wind Direction ', 'WD', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)
        # Sequencial_DIR
    if press:
        press_m1, press_n1, press_nome, press_xlsx, flags_press, estatistico_press, pot_press_xlsx, blox_plot_press = sequencial_press(raw, press_avg, press_max, press_min, press_std, press_avg_dia, lims_press, limi_press, 'Pressure', 'P', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo, es)
        # Sequencial_PRESS
    if prec:
        prec_m1, prec_n1, prec_nome, prec_xlsx, flags_prec, estatistico_prec, pot_prec_xlsx, blox_plot_prec = sequencial_prec(raw, prec_avg, prec_avg_dia, prec_max, 'Precipitation ', 'PR', mes, dia_final, ano, horalocal, dia_mes, nome_arquivo)   
        # Sequencial_PREC

    nome_relatorio = ['Data', 'TEMP', 'UR', 'VEL']
    estatistico_nome = pd.DataFrame({
        'Month': [mes] * 5,
        'Flag': ['Not available', 'Untested', 'Anomalous', 'Suspicious', 'Positive']
    }).T

    bloxplot_nome = pd.DataFrame(['TERMOS', 'Q3', 'Max', 'Mediana', 'Média', 'Min', 'Q1', 'Std'])

    estatistico_met = pd.concat([estatistico_nome, estatistico_temp, estatistico_ur, estatistico_vel], axis=1)
    met_xlsx = pd.concat([temp_xlsx, ur_xlsx.iloc[:, 1], vel_xlsx.iloc[:, 1]], axis=1)
    met_xlsxplot = pd.DataFrame(np.vstack([nome_relatorio, met_xlsx]), columns=range(met_xlsx.shape[1]))

    aux = pd.DataFrame(np.nan, index=[0], columns=range(6))
    flags_met = pd.concat([flags_temp, aux, flags_ur, aux, flags_vel], axis=0)
    pot_met_xlsx = pd.concat([pot_temp_xlsx, pot_ur_xlsx, pot_vel_xlsx], axis=1)

    blox_plot = pd.concat([bloxplot_nome, blox_plot_temp, blox_plot_ur, blox_plot_vel], axis=1)

    # Condição para DIR
    if len(dire) > 0: 
        estatistico_met = pd.concat([estatistico_met, estatistico_dire], axis=1)
        met_xlsx = pd.concat([met_xlsx, dire_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('DIR')
        met_xlsxplot = pd.DataFrame(np.vstack([nome_relatorio, met_xlsx]), columns=range(met_xlsx.shape[1]))
        flags_met = pd.concat([flags_met, flags_dire], axis=0)
        pot_met_xlsx = pd.concat([pot_met_xlsx, pot_dire_xlsx], axis=1)
        blox_plot = pd.concat([blox_plot, blox_plot_dire], axis=1)

    # Condição para PRESS
    if len(press) > 0: 
        estatistico_met = pd.concat([estatistico_met, estatistico_press], axis=1)
        met_xlsx = pd.concat([met_xlsx, press_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('PRESS')
        met_xlsxplot = pd.DataFrame(np.vstack([nome_relatorio, met_xlsx]), columns=range(met_xlsx.shape[1]))
        flags_met = pd.concat([flags_met, flags_press], axis=0)
        pot_met_xlsx = pd.concat([pot_met_xlsx, pot_press_xlsx], axis=1)
        blox_plot = pd.concat([blox_plot, blox_plot_press], axis=1)

    # Condição para PREC
    if len(prec) > 0: 
        estatistico_met = pd.concat([estatistico_met, estatistico_prec], axis=1)
        met_xlsx = pd.concat([met_xlsx, prec_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('PREC')
        met_xlsxplot = pd.DataFrame(np.vstack([nome_relatorio, met_xlsx]), columns=range(met_xlsx.shape[1]))
        flags_met = pd.concat([flags_met, flags_prec], axis=0)
        pot_prec_xlsx = pd.DataFrame(pot_prec_xlsx)
        pot_met_xlsx = pd.concat([pot_met_xlsx, pot_prec_xlsx], axis=1)
        blox_plot = pd.concat([blox_plot, blox_plot_prec], axis=1)


    pd.DataFrame(blox_plot).to_excel(f"{nome_arquivo}_BloxPlot_MET.xlsx", index=False)

    return estatistico_met, met_xlsxplot, flags_met, pot_met_xlsx, blox_plot
