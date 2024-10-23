import numpy as np
import pandas as pd
from testes.teste_limites_fisicos import teste_limites_fisicos
from testes.teste_std_consistencia import teste_std_consistencia
from resultado_var import resultado_var
from potencial_var import potencial_var
from flag_plot import flag_plot
from box_plot import blox_plot
from total_xplot3x import total_xplot3x
from total_xplot3cx import total_xplot3cx
from testes.teste_extremamente_raro import teste_extremamente_raro
from potencial_prec import potencial_prec
from total_xplot3 import total_xplot3
from total_xplot import total_xplot


def sequencial_prec(raw, var_avg, var_avg_dia, prec_max, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo):
    # =================== Informações dos dados brutos ========================
    n, m = raw.shape

    dia_anterior = 1440
    data = raw.iloc[dia_anterior:, 0]

    n_anterior = n
    n = n - dia_anterior

    # =========================== Criação das Flags ===========================
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ============================= Dados Brutos ==============================
    prec_flag1 = 0
    prec_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            prec_flag6 += 1
        else:
            prec_flag1 += 1

    m1 = np.full((n, 1), np.nan)  # Inicializa m1 com NaN
    m1[:, 0] = var_avg  # Atribui var_avg a m1
    n1 = np.full((6, 1), np.nan)  # Inicializa n1 com NaN
    n1[0, 0] = prec_flag1
    n1[1, 0] = 0
    n1[2, 0] = 0
    n1[3, 0] = 0
    n1[4, 0] = 0
    n1[5, 0] = prec_flag6

    nome = ["RAW"]

    # ==================== PRESS - Testes Comparativos =========================

    # =================== Fisicamente Possível ==========================
    lf_prec, lf_prec_flag = teste_limites_fisicos(var_avg, var_avg, prec_max, 0, n)
    m1 = np.column_stack((m1, lf_prec))
    n1 = np.hstack((n1, lf_prec_flag.reshape(-1, 1)))
    nome.append("Fisicamente Possível")

    # =================== Extremamente Raro ==========================
    er_prec, er_prec_flag = teste_extremamente_raro(var_avg, lf_prec, var_avg_dia, dia_anterior, 25, 60, n)  # A lógica é trocada em relação a temperatura
    m1 = np.column_stack((m1, er_prec))
    n1 = np.hstack((n1, er_prec_flag.reshape(-1, 1)))
    nome.append("Extremamente Raro")

    # =================== Extremamente Raro ==========================
    et_prec, et_prec_flag = teste_extremamente_raro(var_avg, er_prec, var_avg_dia, dia_anterior, 100, 1440, n)  # A lógica é trocada em relação a temperatura
    m1 = np.column_stack((m1, er_prec))
    n1 = np.hstack((n1, er_prec_flag.reshape(-1, 1)))
    nome.append("Evolução Temporal")

    # ======= Consolidação dos Resultados ======
    resultado_prec, resultado_flag_prec, flags_prec, estatistico_prec, prec_xlsx = resultado_var(et_prec, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_prec))
    n1 = np.hstack((n1, resultado_flag_prec.reshape(-1, 1)))
    nome.append("Resultado")

    # ======= Cálculo do Potencial =========
    #pot_prec, pot_prec_xlsx = potencial_var(resultado_prec, var_avg, nome_var, var_min, nome_var, horalocal, dia_mes, n)
    pot_prec, pot_prec_xlsx = potencial_prec(resultado_prec, var_avg, nome_var, horalocal, dia_mes, n, nome_arquivo)



    
    blox_plot_prec = blox_plot(resultado_prec, var_avg, nome_arquivo, nome_var, 10, '[nm]', 0, 5, n)
    flag = flag_plot(var_avg, resultado_prec)

    #n, m = var_avg.shape

    for i in range(len(var_avg)):
        if var_avg[i] > 60 or var_avg[i] < 0:
            var_avg[i] = 0
            #var_max[i] = 0
            #var_min[i] = 0
    
    total_xplot3(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 5, 0, '[mm]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot(var_avg, data, 12, titulo, dia_final, mes, ano, 5, 0, '[mm]', 10, 'b', nome_arquivo)




    # ======= Blox Plot =========
    #
    return m1, n1, nome, prec_xlsx, flags_prec, estatistico_prec, pot_prec_xlsx, blox_plot_prec