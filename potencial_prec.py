import numpy as np
import matplotlib.pyplot as plt

def potencial_prec(resultado, var_avg, nome_var, horalocal, dia_mes, n, nome_arquivo):
    # =========================== Criação das Flags ===========================
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 20000

    #==========================================================================  
    #                         Cálculo do Potencial     
    #==========================================================================

    # ======= Var avg min =======  
    var_avg_minuto = np.full(n, np.nan)

    for i in range(n):
        if resultado[i] != flag6 and resultado[i] != flag3:
            var_avg_minuto[i] = var_avg[i]

    # ========================= Dia =============================
    max_dia = max(dia_mes)
    n1 = max_dia * 24
    dia = np.full(n1, np.nan)
    aux = 0
    cont = 0

    for i in range(n):
        if horalocal[i] == 0:
            if cont < 60:
                dia[aux] = dia_mes[i]
                aux += 1
                cont += 1
        else:
            cont = 1

    # ======= Hora =======
    hora = np.zeros(n1)

    cont = 0
    for i in range(n1):
        if cont < 60:
            hora[i] = cont
            cont += 1
        else:
            cont = 0
            hora[i] = cont
            cont += 1

    horay = np.zeros(n1)

    cont = 0
    for i in range(n1):
        if cont < 24:
            horay[i] = cont
            cont += 1
        else:
            cont = 0
            horay[i] = cont
            cont += 1

    # ======= Var avg Hora =======
    var_avg_hora = np.zeros(n1)
    aux = 0
    auxx = 60

    for i in range(n1):
        if auxx < n:
            var_avg_hora[i] = np.sum(var_avg_minuto[aux:auxx])
            aux = auxx
            auxx += 60

    # ======= Prec - sum dia =======  
    prec_dia = np.zeros(max_dia + 1)
    aux = 0
    auxx = 1440

    for i in range(max_dia):
        if auxx <= n + 1440:
            prec_dia[i] = np.sum(var_avg_minuto[aux:auxx])
            aux = auxx
            auxx += 1440

    dia_x = np.arange(1, max_dia + 1)

    # ======= Horax =======
    horax = np.arange(24)

    # ======= Matriz auxiliar =======
    matx_dia = np.full((24, 24), np.nan)
    matxx_dia = np.full((max_dia * 24, 24), np.nan)
    for i in range(24):
        matx_dia[i, i] = 1

    aux = 0
    auxx = 24
    for i in range(max_dia):
        matxx_dia[aux:auxx, :] = matx_dia
        aux += 24
        auxx += 24

    # ======= Var avg Hora =======
    var_avg_med = np.full(24, np.nan)
    var_avg_hora_x = var_avg_hora[:, None] * matxx_dia
    for i in range(24):
        var_avg_med[i] = np.nanmean(var_avg_hora_x[:, i])

    m = np.zeros((24, 2))
    m[:, 0] = horax
    m[:, 1] = var_avg_med

    x = m
    nome = [nome_var, ['Hora', 'Avg']]
    xlsx = [nome] + m.tolist()

    # ======= Plot Prec - sum dia =======  
    dia_x = np.arange(1, max_dia + 1)
    prec_dia = prec_dia[:-1]

    plt.figure(figsize=(12, 6))
    plt.bar(dia_x, prec_dia, color=[0.04, 0, 0.5])
    for i in range(len(prec_dia)):
        plt.text(dia_x[i], prec_dia[i], f'{prec_dia[i]:.0f}', ha='center', va='bottom')

    plt.grid(which='minor', linestyle='--')
    plt.ylim(0, 100)
    plt.ylabel('[mm]')
    plt.xlim(0, max(dia_x) + 1)
    plt.xlabel('Time [day]')
    plt.xticks(dia_x)

    plt.savefig(f'{nome_arquivo}_Prec_dia.pdf', format='pdf')
    plt.savefig(f'{nome_arquivo}_Prec_dia.png', format='png')
    plt.close()

    return x, xlsx