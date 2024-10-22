import numpy as np
import pandas as pd
from testes.teste_limites_fisicos import teste_limites_fisicos
from testes.teste_bsrn import teste_bsrn
from testes.teste_angulo_elevacao import teste_angulo_elevacao
from testes.teste_kt_ghi import teste_kt_ghi
from testes.teste_std_consistencia import teste_std_consistencia
from testes.teste_comparacao_simples import teste_comparacao_simples
from testes.teste_comparacao_completo import teste_comparacao_completo
from testes.teste_clear_sky import teste_clear_sky
from testes.teste_consistencia import teste_consistencia
from testes.teste_persistencia import teste_persistencia
from testes.teste_evolucao_temporal import teste_evolucao_temporal
from testes.teste_extremamente_raro import teste_extremamente_raro
from resultado_var import resultado_var
from potencial_var import potencial_var
from flag_plot import flag_plot
from box_plot import blox_plot
from total_xplot3x import total_xplot3x
from total_xplot3cx import total_xplot3cx
def sequencial_temp(raw, var_avg, var_max, var_min, var_std, var_avg_dia, temp_fp_max, temp_fp_min, titulo, nome_var, mes, dia_final, ano, horalocal, dia_mes, nome_arquivo):

    # =================== Informações dos dados brutos ========================
    n, m = raw.shape

    dia_anterior = 1440
    data = raw.iloc[dia_anterior:, 0]

    n_anterior = n
    n = n - dia_anterior

    print("TAMANHO DE N: ", n)
    print("TAMANHO DE VAR AVG: ", var_avg.shape)

    # =========================== Criação das Flags ===========================
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ============================= Dados Brutos ==============================
    temp_flag1 = 0
    temp_flag6 = 0

    for i in range(n):
        if var_avg[i] == flag6:
            temp_flag6 += 1
        else:
            temp_flag1 += 1



    m1 = np.full(n, np.nan)
    m1 = var_avg
    n1 = np.full((6,1), np.nan)
    n1[0][0] = temp_flag1
    n1[1][0] = 0
    n1[2][0] = 0
    n1[3][0] = 0
    n1[4][0] = 0
    n1[5][0] = temp_flag6

    nome = ["RAW"]

    # ==================== TEMP - Testes Comparativos =========================
    
    # =================== Fisicamente Possível ==========================
    lf_temp, lf_temp_flag = teste_limites_fisicos(var_avg, var_avg, temp_fp_max, temp_fp_min, n)
    m1 = np.column_stack((m1, lf_temp))
    n1 = np.hstack((n1, lf_temp_flag.reshape(-1,1)))
    nome.append("Fisicamente Possível")


    # =================== Extremamente Raro ==========================
    er_temp, er_temp_flag = teste_extremamente_raro(var_avg, lf_temp, var_avg_dia, dia_anterior, 5, 60, n)
    m1 = np.column_stack((m1, er_temp))
    n1 = np.hstack((n1, er_temp_flag.reshape(-1,1)))
    nome.append('Extremamente raro')


    # ============== Desvio Padrão e Consistência de Parâmetros ===============
    std_consistencia, std_consistencia_flag = teste_std_consistencia(er_temp, var_avg, var_max, var_min, var_std, n)
    m1 = np.column_stack((m1, std_consistencia))
    n1 = np.hstack((n1, std_consistencia_flag))
    nome.extend(["Desvio padrão nulo", "Consistência de parâmetros"])

    # ============== Evolução Temporal ===============
    et_temp, et_temp_flag = teste_evolucao_temporal(var_avg, std_consistencia[:, 1], var_avg_dia, dia_anterior, 0.5, 1440, n)
    m1 = np.column_stack((m1, et_temp))
    n1 = np.hstack((n1, et_temp_flag.reshape(-1,1)))
    nome.append('Evolucao Temporal')

    # ======= Consolidação dos Resultados ======
    resultado_temp, resultado_flag_temp, flags_temp, estatistico_temp, temp_xlsx = resultado_var(et_temp, var_avg, nome, nome_var, data, n1, n)
    m1 = np.column_stack((m1, resultado_temp))
    n1 = np.hstack((n1, resultado_flag_temp.reshape(-1,1)))
    nome.append('Resultado')

    # ======= Cálculo do Potencial =========
    pot_temp, pot_temp_xlsx = potencial_var(resultado_temp, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)

    # ======= Box Plot =========
    blox_plot_temp = blox_plot(resultado_temp, var_avg, nome_arquivo, nome_var, 10, '[°C]', 0, 40, n)

    # ===================== PLOT da Variável ==================================
    flag = flag_plot(var_avg, resultado_temp)
    for i in range(n):
        if var_avg[i] > 60:
            var_avg[i] = 0
            var_max[i] = 0
            var_min[i] = 0

    total_xplot3x(var_avg, flag[:, 1], flag[:, 2], data, 1, titulo, nome_var, dia_final, mes, ano, 45, 0, '[°C]', 10, 'b', [1, 0.75, 0.035], 'red', nome_arquivo)
    total_xplot3cx(var_max, var_min, var_avg, data, 2, titulo, dia_final, mes, ano, 45, 0, '[°C]', 10, 'Temp max', 'Temp min', 'Temp avg', nome_arquivo)

    return
    # return m1, n1, nome, temp_xlsx, flags_temp, estatistico_temp, pot_temp_xlsx, blox_plot_temp
