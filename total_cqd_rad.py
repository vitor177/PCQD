import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sequencial_ghi import sequencial_ghi
from sequencial_dhi import sequencial_dhi
from sequencial_bni import sequencial_bni
from sequencial_gri import sequencial_gri
from total_eplot import total_eplot
from total_pplot import total_pplot
from total_xplot3c import total_xplot3c
from total_over_irradiance import total_over_irradiance
#from total_xplotdisx import total_xplot_disx
from total_xplot2c import total_xplot2c
from total_xplotdisx import total_xplotdisx
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

    # is empty ghi2
    if not ghi2:
        ghi_m1, ghi_n1, ghi_nome, ghi_xlsx, flags_ghi, estatistico_ghi, pot_ghi_xlsx, energia_ghi_xlsx = sequencial_ghi(raw_rad, dados, ghi1_avg, ghi1_max, ghi1_min, ghi1_std, ghi1_avg_p, 'Global Horizontal Irradiance ', 'GHI', ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        ghi_over = total_over_irradiance(raw_rad, dados, ghi1, clear_sky, dia_final, mes, ano, 'Overirradiance Events - GHI ', 'GHI', nome_arquivo  )
    if ghi2:
        ghi_m1, ghi_n1, ghi_nome, ghi_xlsx, flags_ghi, estatistico_ghi, pot_ghi_xlsx, energia_ghi_xlsx = sequencial_ghi(raw_rad, dados, ghi1_avg, ghi1_max, ghi1_min, ghi1_std, ghi1_avg_p, 'Global Horizontal Irradiance 1', 'GHI1', ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        ghi2_m1, ghi2_n1, ghi2_nome, ghi2_xlsx, flags_ghi2, estatistico_ghi2, pot_ghi2_xlsx, energia_ghi2_xlsx = sequencial_ghi(raw_rad, dados, ghi2_avg, ghi2_max, ghi2_min, ghi2_std, ghi2_avg_p, 'Global Horizontal Irradiance 2', 'GHi2', ghi1, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        ghi1_over = total_over_irradiance(raw_rad, dados, ghi1, clear_sky, dia_final, mes, ano, 'Overirradiance Events - GHI 1', 'GHI1', nome_arquivo  )
        ghi2_over = total_over_irradiance(raw_rad, dados, ghi2, clear_sky, dia_final, mes, ano, 'Overirradiance Events - GHI 2', 'GHI2', nome_arquivo  )
    if ghi3:
        ghi3_m1, ghi3_n1, ghi3_nome, ghi3_xlsx, flags_ghi3, estatistico_ghi3, pot_ghi3_xlsx, energia_ghi3_xlsx = sequencial_ghi(raw_rad, dados, ghi3_avg, ghi3_max, ghi3_min, ghi3_std, ghi3_avg_p, 'Global Horizontal 3', 'GHI3', ghi1, ghi2, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        ghi3_over = total_over_irradiance(raw_rad, dados, ghi3, clear_sky, dia_final, mes, ano, 'Overirradiance Events - GHI 3 ', 'GHI3', nome_arquivo)
    if dhi:
        dhi_m1, dhi_n1, dhi_nome, dhi_xlsx, flags_dhi, estatistico_dhi, pot_dhi_xlsx, energia_dhi_xlsx = sequencial_dhi(raw_rad, dados, dhi_avg, dhi_max, dhi_min, dhi_std, dhi_avg_p, 'Diffuse Horizontal Irradiance ', 'DHI', ghi1, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
        bni_m1, bni_n1, bni_nome, bni_xlsx, flags_bni, estatistico_bni, pot_bni_xlsx, energia_bni_xlsx = sequencial_bni(raw_rad, dados, bni_avg, bni_max, bni_min, bni_std, bni_avg_p, 'Bean Normal Irradiance ', 'BNI', ghi1, ghi2, ghi3, poa, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo)
    if gri1 and not gri2:
        gri1_m1, gri1_n1, gri1_nome, gri1_xlsx, flags_gri1, estatistico_gri1, pot_gri1_xlsx, energia_gri1_xlsx = sequencial_gri(raw_rad, dados, gri1_avg, gri1_max, gri1_min, gri1_std, gri1_avg, 'Global Horizontal Reflective  ','GRI', gri2, clear_sky, mes, dia_final, ano, nome_arquivo)
    if gri2:
        gri1_m1, gri1_n1, gri1_nome, gri1_xlsx, flags_gri1, estatistico_gri1, pot_gri1_xlsx, energia_gri1_xlsx = sequencial_gri(raw_rad, dados, gri1_avg, gri1_max, gri1_min, gri1_std, gri1_avg, 'Global Horizontal Reflective  1 ','GRI 1', gri2, clear_sky, mes, dia_final, ano, nome_arquivo)
        gri2_m1, gri2_n1, gri2_nome, gri2_xlsx, flags_gri2, estatistico_gri2, pot_gri2_xlsx, energia_gri2_xlsx = sequencial_gri(raw_rad, dados, gri2_avg, gri2_max, gri2_min, gri2_std, gri2_avg, 'Global Horizontal Reflective  2 ','GRI 2', gri1, clear_sky, mes, dia_final, ano, nome_arquivo)

    # Lista para armazenar os nomes das colunas
    nome_relatorio = ['Data', 'GHI1']

    estatistico_nome = pd.DataFrame({
        'Month': [mes] * 5,
        'Flag': ['Not available', 'Untested', 'Anomalous', 'Suspicious', 'Positive']
    }).T
    
    # Estatístico GHI
    estatistico_ghi = pd.concat([estatistico_nome, estatistico_ghi], axis=1)
    energia_ghi1_xlsx = energia_ghi_xlsx
    pot_ghi1_xlsx = pot_ghi_xlsx

    # Condição para GHI2
    if len(ghi2) > 0:
        estatistico_ghi = pd.concat([estatistico_ghi, estatistico_ghi2], axis=1)
        ghi_xlsx = pd.concat([ghi_xlsx, ghi2_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('GHI2')
        energia_ghi_xlsx = pd.concat([energia_ghi_xlsx, energia_ghi2_xlsx], axis=1)
        pot_ghi_xlsx = pd.concat([pot_ghi_xlsx, pot_ghi2_xlsx], axis=1)
        flags_ghi = pd.concat([flags_ghi, flags_ghi2], axis=0)


    # Condição para GHI3
    if len(ghi3) > 0:
        estatistico_ghi = pd.concat([estatistico_ghi, estatistico_ghi3], axis=1)
        ghi_xlsx = pd.concat([ghi_xlsx, ghi3_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('GHI3')
        energia_ghi_xlsx = pd.concat([energia_ghi_xlsx, energia_ghi3_xlsx], axis=1)
        pot_ghi_xlsx = pd.concat([pot_ghi_xlsx, pot_ghi3_xlsx], axis=1)
        flags_ghi = pd.concat([flags_ghi, flags_ghi3], axis=0)

    # Condição para DHI
    if len(dhi) > 0:
        estatistico_ghi = pd.concat([estatistico_ghi, estatistico_bni, estatistico_dhi], axis=1)
        ghi_xlsx = pd.concat([ghi_xlsx, bni_xlsx.iloc[:, 1], dhi_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.extend(['BNI', 'DHI'])
        energia_ghi_xlsx = pd.concat([energia_ghi_xlsx, energia_bni_xlsx, energia_dhi_xlsx], axis=1)
        pot_ghi_xlsx = pd.concat([pot_ghi_xlsx, pot_bni_xlsx, pot_dhi_xlsx], axis=1)


        flags_ghi = pd.concat([flags_ghi, flags_bni, flags_dhi], axis=0)


    # Condição para GRI1
    if len(gri1) > 0:
        estatistico_ghi = pd.concat([estatistico_ghi, estatistico_gri1], axis=1)
        ghi_xlsx = pd.concat([ghi_xlsx, gri1_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('GRI1')
        energia_ghi_xlsx = pd.concat([energia_ghi_xlsx, energia_gri1_xlsx], axis=1)
        pot_ghi_xlsx = pd.concat([pot_ghi_xlsx, pot_gri1_xlsx], axis=1)
        flags_ghi = pd.concat([flags_ghi, flags_gri1], axis=0)

    # Condição para GRI2
    if len(gri2) > 0:
        estatistico_ghi = pd.concat([estatistico_ghi, estatistico_gri2], axis=1)
        ghi_xlsx = pd.concat([ghi_xlsx, gri2_xlsx.iloc[:, 1]], axis=1)
        nome_relatorio.append('GRI2')
        energia_ghi_xlsx = pd.concat([energia_ghi_xlsx, energia_gri2_xlsx], axis=1)
        pot_ghi_xlsx = pd.concat([pot_ghi_xlsx, pot_gri2_xlsx], axis=1)
        flags_ghi = pd.concat([flags_ghi, flags_gri2], axis=0)

    # Salvando os dados como arquivos Excel
    #energia_ghi_xlsx.columns = nome_relatorio  # Define os nomes das colunas com base na lista nome_relatorio
    energia_ghi_xlsx.to_excel(f'{nome_arquivo}_Energia.xlsx', index=False)

    ghi_xlsx.columns = nome_relatorio


    #flags_ghi.to_excel(f'{nome_arquivo}_VEJAI_VITAO.xlsx', index=False)
    if len(ghi2) == 0 and len(ghi3) == 0:
        total_eplot(energia_ghi1_xlsx, [], [], 2, 'Energy Fraction ', 'GHI', 'GHI 2', 'GHI 3', nome_arquivo)
        total_pplot(pot_ghi_xlsx, [], [], 3, mes, nome_arquivo)

    if len(ghi2) > 0 and len(ghi3) == 0:
        for i in range(n):
            if ghi1_avg[i] > 2000:
                ghi1_avg[i] = 0
            if ghi2_avg[i] > 2000:
                ghi2_avg[i] = 0
        total_xplot2c(ghi1_avg, ghi2_avg, data, 1, 'Comparison of Measured GHI Values ', dia_final, mes, ano, 1800, 0, 'W/m²', 10, 'GHI1 avg', 'GHI2 avg', nome_arquivo)
        vazio = []
        total_eplot(energia_ghi1_xlsx, energia_ghi2_xlsx, vazio, 2, 'Energy Fraction of Variables ', 'GHI 1','GHI 2 ','GHI 3', nome_arquivo)
        total_pplot(pot_ghi1_xlsx, pot_ghi2_xlsx, vazio, 3, mes, nome_arquivo)
        total_xplotdisx(ghi1_avg, ghi2_avg, 'GHI 1', 'GHI 2', 'W/m²', 4, 1500, nome_arquivo)

    
    if len(ghi3) > 0:  # Verifica se gh3 não está vazio
        for i in range(n):
            if ghi1_avg[i] > 2000:
                ghi1_avg[i] = 0
            if ghi2_avg[i] > 2000:
                ghi2_avg[i] = 0
            if ghi3_avg[i] > 2000:
                ghi3_avg[i] = 0
                
        plt.close('all')

        # Chama as funções para gerar gráficos
        total_xplot3c(ghi1_avg, ghi2_avg, ghi3_avg, data, 1, 'Comparison of Measured GHI Values ', dia_final, mes, ano, 1800, 0, 'W/m²', 10, 'GHI1 avg', 'GHI2 avg', 'GHI3 avg', nome_arquivo)
        total_eplot(energia_ghi1_xlsx, energia_ghi2_xlsx, energia_ghi3_xlsx, 2, 'Energy Fraction of Variables ', 'GHI 1', 'GHI 2', 'GHI 3', nome_arquivo)
        total_pplot(pot_ghi1_xlsx, pot_ghi2_xlsx, pot_ghi3_xlsx, 3, mes, nome_arquivo)    
        total_xplotdisx(ghi1_avg, ghi2_avg, 'GHI 1', 'GHI 2', 'W/m²', 4, 1500, nome_arquivo)
        total_xplotdisx(ghi1_avg, ghi3_avg, 'GHI 1', 'GHI 3', 'W/m²', 5, 1500, nome_arquivo)
        total_xplotdisx(ghi2_avg, ghi3_avg, 'GHI 2', 'GHI 3', 'W/m²', 6, 1500, nome_arquivo)

    if len(dhi) > 0:  # Verifica se dhi não está vazio
        for i in range(n):
            if cosAZS[i] < 0:
                cosAZS[i] = 0

        bhi_avg = bni_avg * cosAZS  # Calcula bhi_avg
        for i in range(n):
            if ghi1_avg[i] > 2000:
                ghi1_avg[i] = 0
            if bni_avg[i] > 1500:
                bni_avg[i] = 0
            if dhi_avg[i] > 1500:
                dhi_avg[i] = 0

        plt.close('all')
        
        # Chama a função para gerar gráficos de comparação
        total_xplot3c(ghi1_avg, bni_avg, dhi_avg, data, 1, 'Comparison between radiometric variables ', dia_final, mes, ano, 1400, 0, 'W/m²', 10, 'GHI avg', 'BNI avg', 'DHI avg', nome_arquivo)

    return estatistico_ghi, ghi_xlsx, flags_ghi, pot_ghi_xlsx, energia_ghi1_xlsx


# 2, 4 e 5 CHECK


# eplot, pplot, xplot2c, xplotdisx, xplot3c