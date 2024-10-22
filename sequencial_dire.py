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
from testes.teste_evolucao_temporal import teste_evolucao_temporal


def sequencial_dire(raw, var_avg, var_max, var_min, var_std, var_avg_dia, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo):
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
    dir_flag1 = 0
    dir_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            dir_flag6 += 1
        else:
            dir_flag1 += 1

    m1 = np.full(n, np.nan)  # Inicializa m1 com NaN
    m1 = var_avg  # Atribui var_avg a m1
    n1 = np.full((6, 1), np.nan)  # Inicializa n1 com NaN
    n1[0][0] = dir_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = dir_flag6

    nome = ["RAW"]

    # ==================== DIR - Testes Comparativos =========================

    # =================== Fisicamente Possível ==========================
    lf_dir, lf_dir_flag = teste_limites_fisicos(var_avg, var_avg, 360, 0, n)
    m1 = np.column_stack((m1, lf_dir))
    n1 = np.hstack((n1, lf_dir_flag.reshape(-1, 1)))
    nome.append("Fisicamente Possível")

    # =================== Extremamente Raro ==========================
    er_dir, er_dir_flag = teste_evolucao_temporal(var_avg, lf_dir, var_avg_dia, dia_anterior, 1, 180, n)
    m1 = np.column_stack((m1, er_dir))
    n1 = np.hstack((n1, er_dir_flag.reshape(-1, 1)))
    nome.append("Extremamente Raro")

    # ============== Desvio Padrão e Consistência de Parâmetros ===============
    std_consistencia, std_consistencia_flag = teste_std_consistencia(er_dir, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    # ============== Evolução Temporal ===============
    et_dir, et_dir_flag = teste_evolucao_temporal(var_avg, std_consistencia[:, 1], var_avg_dia, dia_anterior, 10, 1080, n)
    m1 = np.column_stack((m1, et_dir))
    n1 = np.hstack((n1, et_dir_flag.reshape(-1, 1)))
    nome.append("Evolução Temporal")

    # ======= Consolidação dos Resultados ======
    resultado_dir, resultado_flag_dir, flags_dir, estatistico_dir, dir_xlsx = resultado_var(et_dir, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_dir))
    n1 = np.hstack((n1, resultado_flag_dir.reshape(-1, 1)))
    nome.append("Resultado")

    # ======= Cálculo do Potencial =========
    pot_dir, pot_dir_xlsx = potencial_var(resultado_dir, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # ===================== PLOT da Variável ==================================
    flag = flag_plot(var_avg, resultado_dir)
    for i in range(n):
        if var_avg[i] > 360:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0
        if var_avg[i] < 0:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0

    total_xplot3x(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 360, 0, '[°]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot3cx(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 360, 0, '[°]', 10, 'WD max', 'WD min', 'WD avg', nome_arquivo)

    # ======= Blox Plot =========
    blox_plot_dir = blox_plot(resultado_dir, var_avg, nome_arquivo, nome_var, 10, '[°]', 0, 360, n)

    return m1, n1, nome, dir_xlsx, flags_dir, estatistico_dir, pot_dir_xlsx, blox_plot_dir
