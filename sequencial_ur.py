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
import matplotlib.pyplot as plt

def sequencial_ur(raw, var_avg, var_max, var_min, var_std, var_avg_dia, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo):
    # =================== Informações dos dados brutos ========================
    n, m = raw.shape

    dia_anterior = 1440
    data = raw.iloc[dia_anterior:, 0]

    n_anterior = n
    n = n - dia_anterior

    # =========================== Criação das Flags ===========================
    flag6 = 60000
    flag1 = 10000

    # ============================= Dados Brutos ==============================
    ur_flag1 = 0
    ur_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            ur_flag6 += 1
        else:
            ur_flag1 += 1

    m1 = np.full(n, np.nan)  # Inicializa m1 com NaN
    m1 = var_avg  # Atribui var_avg a m1
    n1 = np.full((6, 1), np.nan)  # Inicializa n1 com NaN
    n1[0][0] = ur_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = ur_flag6

    nome = ["RAW"]

    # ==================== UR - Testes Comparativos =========================

    # =================== Fisicamente Possível ==========================
    lf_ur, lf_ur_flag = teste_limites_fisicos(var_avg, var_avg, 100, 0, n)
    m1 = np.column_stack((m1, lf_ur))
    n1 = np.hstack((n1, lf_ur_flag.reshape(-1, 1)))
    nome.append("Fisicamente Possível")

    # ============== Desvio Padrão e Consistência de Parâmetros ===============
    std_consistencia, std_consistencia_flag = teste_std_consistencia(lf_ur, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    # ======= Consolidação dos Resultados ======
    resultado_ur, resultado_flag_ur, flags_ur, estatistico_ur, ur_xlsx = resultado_var(std_consistencia[:, 1], var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_ur))
    n1 = np.hstack((n1, resultado_flag_ur.reshape(-1, 1)))
    nome.append("Resultado")

    # ======= Cálculo do Potencial =========
    pot_ur, pot_ur_xlsx = potencial_var(resultado_ur, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # ===================== PLOT da Variável ==================================
    flag = flag_plot(var_avg, resultado_ur)
    for i in range(n):
        if var_avg[i] > 100:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0
        if var_avg[i] < 0:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0

    total_xplot3x(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 100, 0, '[%]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot3cx(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 100, 0, '[%]', 10, 'UR max', 'UR min', 'UR avg', nome_arquivo)

    # ======= Blox Plot =========
    blox_plot_ur = blox_plot(resultado_ur, var_avg, nome_arquivo, nome_var, 10, '[%]', 0, 100, n)

    return m1, n1, nome, ur_xlsx, pd.DataFrame(flags_ur.T), pd.DataFrame(estatistico_ur), pot_ur_xlsx, pd.DataFrame(blox_plot_ur)
#     return m1, n1, nome, ghi1_xlsx, pd.DataFrame(flags_ghi1.T), pd.DataFrame(estatistico_ghi1), pot_ghi1_xlsx, energia_ghi1_xlsx
