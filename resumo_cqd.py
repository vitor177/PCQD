import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def resumo_cqd(est_rad, est_met, rad_xlsxplot, met_xlsxplot, flags_rad, flags_met, pot_rad_xlsx, pot_met_xlsx, nome_arquivo):
 # pd.concat([pot_met_xlsx, pot_prec_xlsx], axis=1)


    print("VITAAAAAAAAAAAAAAAO: ", est_rad)

    aux = pd.concat([flags_rad, flags_met])  # Cria um array
    pd.DataFrame(aux).to_excel(f"{nome_arquivo}_Relatorio.xlsx", index=False, header=None)

    aux = pd.concat([pot_rad_xlsx, pot_met_xlsx], axis=1)
    pd.DataFrame(aux).to_excel(f"{nome_arquivo}_Potencial.xlsx", index=False)

    novos_nomes_colunas = met_xlsxplot.iloc[0].tolist()

    met_xlsxplot = met_xlsxplot.iloc[1:].reset_index(drop=True)

    met_xlsxplot.columns = novos_nomes_colunas

    aux = pd.concat([rad_xlsxplot, met_xlsxplot], axis=1)
    pd.DataFrame(aux).to_excel(f"{nome_arquivo}_Resultado_Flags.xlsx", index=False)