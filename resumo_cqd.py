import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def resumo_cqd(est_rad, est_met, rad_xlsxplot, met_xlsxplot, flags_rad, flags_met, pot_rad_xlsx, pot_met_xlsx, nome_arquivo):
 # pd.concat([pot_met_xlsx, pot_prec_xlsx], axis=1)

    aux = pd.concat([flags_rad, flags_met])  # Cria um array
    pd.DataFrame(aux).to_excel(f"{nome_arquivo}_Relatorio.xlsx", index=False)