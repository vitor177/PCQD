import numpy as np
import pandas as pd

def resultado_var(var_ant, var_avg, nome, nome_var, data, flags, n):
    flag6 = 60000
    flag5 = 50000
    flag4 = 40000
    flag3 = 30000
    flag2 = 20000
    flag1 = 10000

    # ============================= Resultado =================================
    resultado = np.full(n, np.nan)
    resultado_flag6 = 0
    resultado_flag5 = 0
    resultado_flag4 = 0
    resultado_flag3 = 0
    resultado_flag2 = 0
    resultado_flag1 = 0

    for i in range(n):
        if var_ant[i] == flag6:
            resultado[i] = flag6
            resultado_flag6 += 1
        elif var_ant[i] == flag5:
            resultado[i] = flag5
            resultado_flag5 += 1
        elif var_ant[i] in (flag4, flag3):
            resultado[i] = flag3
            resultado_flag3 += 1
        elif var_ant[i] == flag2:
            resultado[i] = flag2
            resultado_flag2 += 1
        else:
            resultado[i] = flag1
            resultado_flag1 += 1

    x = resultado

    y = np.array([resultado_flag1, resultado_flag2, resultado_flag3, resultado_flag4, resultado_flag5, resultado_flag6])

    # =========================================================================
    #                       Consolidação das Flags 
    # =========================================================================
    aux = np.column_stack([data, resultado])

    for i in range(n):
        if aux[i, 1] == flag6:
            aux[i, 1] = 'Flag6'
        elif aux[i, 1] == flag5:
            aux[i, 1] = 'Flag5'
        elif aux[i, 1] == flag4:
            aux[i, 1] = 'Flag4'
        elif aux[i, 1] == flag3:
            aux[i, 1] = 'Flag3'
        elif aux[i, 1] == flag2:
            aux[i, 1] = 'Flag2'
        elif aux[i, 1] == flag1:
            aux[i, 1] = 'Flag1'

    xlsx = pd.DataFrame(aux)
    # Salvar XLSX (descomente a linha abaixo se quiser salvar como Excel)
    # xlsx.to_excel('Resultado.xlsx', index=False, header=False)

    # ========= Organização da planilha =======
    flags = np.column_stack([flags, y])
    aux_organizado = np.zeros((5, flags.shape[1]))

    aux_organizado[0, :] = flags[-1, :]
    aux_organizado[1, :] = flags[-2, :]
    aux_organizado[2, :] = flags[-3, :] + flags[-4, :]
    aux_organizado[3, :] = flags[-5, :]
    aux_organizado[4, :] = flags[-6, :]

    # ========= Ajustando para o Relatório =======
    ref = aux_organizado

    # ========== Faz o resumo das Flags da variável ==========
    estatistico = ref[:, -1]
    soma = np.sum(estatistico)
    estatistico = np.column_stack([estatistico, estatistico / soma])

    auxx = [nome_var, '%']
    estatistico = np.row_stack([auxx, estatistico])

    # Salvar estatístico (descomente a linha abaixo se quiser salvar como Excel)
    # pd.DataFrame(estatistico).to_excel(f'Estatistico_{nome_var}.xlsx', index=False, header=False)

    # ============ Consolidação das Flags ====================
    n1 = np.column_stack([aux_organizado])

    nome.append('Resultado')
    auxx_flags = ['Não disponível', 'Não testado', 'Anômalo', 'Suspeito', 'Bom']

    n1 = np.column_stack([auxx_flags, n1])
    n1 = np.row_stack([[nome_var] + nome, n1])

    # Salvar N1 (descomente a linha abaixo se quiser salvar como Excel)
    # pd.DataFrame(n1).to_excel(f'Flags_{nome_var}.xlsx', index=False, header=False)

    return x, y, n1, estatistico, xlsx
