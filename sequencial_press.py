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


def sequencial_press(raw, var_avg, var_max, var_min, var_std, var_avg_dia, limS, limI, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo, es):
    # =================== Informações dos dados brutos ========================
    n, m = raw.shape

    dia_anterior = 1440
    data = raw.iloc[dia_anterior:, 0].to_numpy()

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
    press_flag1 = 0
    press_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            press_flag6 += 1
        else:
            press_flag1 += 1

    m1 = np.full((n, 1), np.nan)  # Inicializa m1 com NaN
    m1[:, 0] = var_avg  # Atribui var_avg a m1
    n1 = np.full((6, 1), np.nan)  # Inicializa n1 com NaN
    n1[0, 0] = press_flag1
    n1[1, 0] = 0
    n1[2, 0] = 0
    n1[3, 0] = 0
    n1[4, 0] = 0
    n1[5, 0] = press_flag6

    nome = ["RAW"]

    # ==================== PRESS - Testes Comparativos =========================

    # =================== Fisicamente Possível ==========================
    lf_press, lf_press_flag = teste_limites_fisicos(var_avg, var_avg, limS, limI, n)
    m1 = np.column_stack((m1, lf_press))
    n1 = np.hstack((n1, lf_press_flag.reshape(-1, 1)))
    nome.append("Fisicamente Possível")

    # =================== Extremamente Raro ==========================
    er_press, er_press_flag = teste_extremamente_raro(var_avg, lf_press, var_avg_dia, dia_anterior, 6, 360, n)  # A lógica é trocada em relação a temperatura
    m1 = np.column_stack((m1, er_press))
    n1 = np.hstack((n1, er_press_flag.reshape(-1, 1)))
    nome.append("Extremamente Raro")

    # ============== Desvio Padrão e Consistência de Parâmetros ===============
    std_consistencia, std_consistencia_flag = teste_std_consistencia(er_press, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    # ======= Consolidação dos Resultados ======
    resultado_press, resultado_flag_press, flags_press, estatistico_press, press_xlsx = resultado_var(std_consistencia[:, 1], var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_press))
    n1 = np.hstack((n1, resultado_flag_press.reshape(-1, 1)))
    nome.append("Resultado")

    # ======= Cálculo do Potencial =========
    pot_press, pot_press_xlsx = potencial_var(resultado_press, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # ===================== PLOT da Variável ==================================
    flag = flag_plot(var_avg, resultado_press)
    
    limSpress = int(round(limS))
    limIpress = int(round(limI))

    if es == 'SPES01':
        limSpress = 960
        limIpress = 945

    for i in range(n):
        if var_avg[i] > 1100:
            var_avg[i] = limSpress
            var_max[i] = 0
            var_min[i] = 0
        if var_avg[i] < 900:
            var_avg[i] = limSpress
            var_max[i] = 0
            var_min[i] = 0

    blox_plot_press = blox_plot(resultado_press, var_avg, nome_arquivo, nome_var, 10, '[hPa]', limIpress, limSpress, n)


    total_xplot3x(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, limSpress, limIpress, '[hPa]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot3cx(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, limSpress, limIpress, '[hPa]', 10, 'P max', 'P min', 'P avg', nome_arquivo)

    # ======= Blox Plot =========
    return m1, n1, nome, press_xlsx, flags_press, estatistico_press, pot_press_xlsx, blox_plot_press
