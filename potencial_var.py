import numpy as np
import pandas as pd

def potencial_var(resultado, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n):
    # =========================== Criação das Flags ===========================
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ========================== Cálculo do Potencial ==========================
    
    # ======= Var avg min =======
    var_avg_minuto = np.full(n, np.nan)
    var_avg_minuto[(resultado != flag6) & (resultado != flag3)] = var_avg[(resultado != flag6) & (resultado != flag3)]
    
    # ======= Var max min =======
    var_max_minuto = np.full(n, np.nan)
    var_max_minuto[(resultado != flag6) & (resultado != flag3)] = var_max[(resultado != flag6) & (resultado != flag3)]
    
    # ======= Var min min =======
    var_min_minuto = np.full(n, np.nan)
    var_min_minuto[(resultado != flag6) & (resultado != flag3)] = var_min[(resultado != flag6) & (resultado != flag3)]
    
    # ========================= Dia ==============================
    max_dia = np.max(dia_mes)
    n1 = max_dia * 24
    dia = np.full(n1, np.nan)
    aux = 0
    cont = 1

    for i in range(n):
        if horalocal[i] == 0:
            if cont < 60:
                dia[aux] = dia_mes[i]
                aux += 1
                cont += 1
        else:
            cont = 1
        
    # ======= Hora =======
    hora = np.arange(n1) % 60
    horay = np.arange(n1) // 60 % 24
    
    # ======= Var avg Hora =======
    var_avg_hora = np.zeros(n1)
    aux = 0
    auxx = 60

    for i in range(n1):
        if auxx < n:
            var_avg_hora[i] = np.nanmean(var_avg_minuto[aux:auxx])
            aux = auxx
            auxx += 60
    
    # ======= Var max Hora =======
    var_max_hora = np.zeros(n1)
    aux = 0
    auxx = 60

    for i in range(n1):
        if auxx < n:
            var_max_hora[i] = np.nanmean(var_max_minuto[aux:auxx])
            aux = auxx
            auxx += 60
    
    # ======= Var min Hora =======
    var_min_hora = np.zeros(n1)
    aux = 0
    auxx = 60

    for i in range(n1):
        if auxx < n:
            var_min_hora[i] = np.nanmean(var_min_minuto[aux:auxx])
            aux = auxx
            auxx += 60
    
    # ======= Horax =======
    horax = np.arange(24)

    # ======= Matriz auxiliar =======
    matx_dia = np.full((24, 24), np.nan)
    matxx_dia = np.full((max_dia * 24, 24), np.nan)
    np.fill_diagonal(matx_dia, 1)
    
    aux = 0
    auxx = 24
    for i in range(max_dia):
        matxx_dia[aux:auxx, :] = matx_dia
        aux += 24
        auxx += 24
    
    # ======= Var avg Hora =======
    var_avg_med = np.nanmean(var_avg_hora.reshape(-1, 24), axis=0)
    
    # ======= Var max Hora =======
    var_max_med = np.nanmean(var_max_hora.reshape(-1, 24), axis=0)
    
    # ======= Var min Hora =======
    var_min_med = np.nanmean(var_min_hora.reshape(-1, 24), axis=0)
    
    # Construindo a matriz de resultado
    M = np.zeros((24, 4))
    M[:, 0] = horax
    M[:, 1] = var_avg_med
    M[:, 2] = var_max_med
    M[:, 3] = var_min_med

    # Convertendo para dataframe para facilitar a manipulação
    M_df = pd.DataFrame(M, columns=['Hora', 'Avg', 'Max', 'Min'])
    M_df.insert(0, 'Nome', nome_var)

    # Para exportar para Excel (caso necessário)

    pd.DataFrame(M_df).to_excel(f'Potencial{nome_var}.xlsx', index=False)


    return M, M_df

# Exemplo de uso
# X, XLSX = potencial_var(Resultado, var_avg, var_max, var_min, nome_var, horalocal, dia_mes, n)
