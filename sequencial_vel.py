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
from testes.teste_evolucao_temporal import teste_evolucao_temporal


def sequencial_vel(raw, var_avg, var_max, var_min, var_std, var_avg_dia, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo):
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
    vel_flag1 = 0
    vel_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            vel_flag6 += 1
        else:
            vel_flag1 += 1

    m1 = np.full(n, np.nan)  # Inicializa m1 com NaN
    m1 = var_avg  # Atribui var_avg a m1
    n1 = np.full((6, 1), np.nan)  # Inicializa n1 com NaN
    n1[0][0] = vel_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = vel_flag6

    nome = ["RAW"]

    # ==================== VEL - Testes Comparativos =========================

    # =================== Fisicamente Possível ==========================
    lf_vel, lf_vel_flag = teste_limites_fisicos(var_avg, var_avg, 25, 0, n)
    m1 = np.column_stack((m1, lf_vel))
    n1 = np.hstack((n1, lf_vel_flag.reshape(-1, 1)))
    nome.append("Fisicamente Possível")

    # =================== Extremamente Raro ==========================
    er_vel, er_vel_flag = teste_evolucao_temporal(var_avg, lf_vel, var_avg_dia, dia_anterior, 0.1, 180, n)  # Ajuste a função conforme necessário
    m1 = np.column_stack((m1, er_vel))
    n1 = np.hstack((n1, er_vel_flag.reshape(-1, 1)))
    nome.append("Extremamente Raro")

    # ============== Desvio Padrão e Consistência de Parâmetros ===============
    std_consistencia, std_consistencia_flag = teste_std_consistencia(er_vel, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    # ============== Evolução Temporal ===============
    et_vel, et_vel_flag = teste_evolucao_temporal(var_avg, std_consistencia[:, 1], var_avg_dia, dia_anterior, 0.5, 720, n)
    m1 = np.column_stack((m1, et_vel))
    n1 = np.hstack((n1, et_vel_flag.reshape(-1, 1)))
    nome.append("Evolução Temporal")

    # ======= Consolidação dos Resultados ======
    resultado_vel, resultado_flag_vel, flags_vel, estatistico_vel, vel_xlsx = resultado_var(et_vel, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_vel))
    n1 = np.hstack((n1, resultado_flag_vel.reshape(-1, 1)))
    nome.append("Resultado")

    # ======= Cálculo do Potencial =========
    pot_vel, pot_vel_xlsx = potencial_var(resultado_vel, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # ===================== PLOT da Variável ==================================
    flag = flag_plot(var_avg, resultado_vel)
    for i in range(n):
        if var_avg[i] > 10:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0
        if var_avg[i] < 0:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0

    total_xplot3x(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 20, 0, '[m/s]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot3cx(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 20, 0, '[m/s]', 10, 'WS max', 'WS min', 'WS avg', nome_arquivo)

    # ======= Blox Plot =========
    blox_plot_vel = blox_plot(resultado_vel, var_avg, nome_arquivo, nome_var, 10, '[m/s]', 0, 25, n)

    return m1, n1, nome, vel_xlsx, flags_vel, estatistico_vel, pot_vel_xlsx, blox_plot_vel
