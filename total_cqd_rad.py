import numpy as np
import pandas as pd

def total_cqd_rad(raw_rad, raw_met, dados, ghi1, ghi2, ghi3, poa, gri1, gri2, dhi, bni, clear_sky, mes, dia_final, ano, nome_arquivo, es):
    #data = raw_rad.iloc[:, 0].to_numpy()


    start_row = 1440-20

    ghi1_avg = raw_rad.iloc[:, ghi1[0]]
    ghi1_max = raw_rad.iloc[:, ghi1[1]]
    #ghi1_min = raw_rad.iloc[:, ghi1[2]]
    #ghi1_std = raw_rad.iloc[:, ghi1[3]]
    ghi1_avg_p = raw_rad.iloc[start_row, ghi1[0]]


    return ghi1_avg, ghi1_max, ghi1_avg_p


# function  [Estatistico_GHI,GHI_XLSXplot,Flags_GHI,Pot_GHI_xlsx,Energia_GHI_xlsx] = 
# TOTAL_CQD_RAD(RAW_RAD,RAW_MET,DADOS,GHI1,GHI2,GHI3,POA,GRI1,GRI2,DHI,BNI,Clear_sky,mes,dia_final,ano,Nome_Arquivo,ES)