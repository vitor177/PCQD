import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def total_pplot(variavel1, variavel2, variavel3, num_figura, mes, nome_arquivo):

    variavel1 = pd.DataFrame(variavel1)
    variavel2 = pd.DataFrame(variavel2) if variavel2 is not None else pd.DataFrame()
    variavel3 = pd.DataFrame(variavel3) if variavel3 is not None else pd.DataFrame()
    cor1 = 'red'
    cor2 = [0.12, 0.64, 0.82]
    cor3 = [1, 0.75, 0.035]

    ghi_avg_med = np.full(24, np.nan)
    ghi_max_med = np.full(24, np.nan)
    ghi_min_med = np.full(24, np.nan)

    ghi1_avg = np.array(variavel1.iloc[:, 2], dtype=float)
    ghi1_max = np.array(variavel1.iloc[:, 3], dtype=float)
    ghi1_min = np.array(variavel1.iloc[:, 4], dtype=float)

    if variavel2.empty and variavel3.empty:
        ghi_avg_med = ghi1_avg
        ghi_max_med = ghi1_max
        ghi_min_med = ghi1_min
        ghi_avg_med[ghi_avg_med < 0] = 0
        ghi_max_med[ghi_max_med < 0] = 0
        ghi_min_med[ghi_min_med < 0] = 0

    if not variavel2.empty and variavel3.empty:
        ghi2_avg = np.array(variavel2.iloc[:, 2], dtype=float)
        ghi2_max = np.array(variavel2.iloc[:, 3], dtype=float)
        ghi2_min = np.array(variavel2.iloc[:, 4], dtype=float)
        for i in range(24):
            ghi_avg_med[i] = np.nanmean([ghi1_avg[i], ghi2_avg[i]])
            ghi_max_med[i] = np.nanmean([ghi1_max[i], ghi2_max[i]])
            ghi_min_med[i] = np.nanmean([ghi1_min[i], ghi2_min[i]])
            if ghi_avg_med[i] < 0:
                ghi_avg_med[i] = 0
                ghi_max_med[i] = 0
                ghi_min_med[i] = 0

    if not variavel2.empty and not variavel3.empty:
        ghi2_avg = np.array(variavel2.iloc[:, 2], dtype=float)
        ghi2_max = np.array(variavel2.iloc[:, 3], dtype=float)
        ghi2_min = np.array(variavel2.iloc[:, 4], dtype=float)
        ghi3_avg = np.array(variavel3.iloc[:, 2], dtype=float)
        ghi3_max = np.array(variavel3.iloc[:, 3], dtype=float)
        ghi3_min = np.array(variavel3.iloc[:, 4], dtype=float)
        for i in range(24):
            ghi_avg_med[i] = np.nanmean([ghi1_avg[i], ghi2_avg[i], ghi3_avg[i]])
            ghi_max_med[i] = np.nanmean([ghi1_max[i], ghi2_max[i], ghi3_max[i]])
            ghi_min_med[i] = np.nanmean([ghi1_min[i], ghi2_min[i], ghi3_min[i]])
            if ghi_avg_med[i] < 0:
                ghi_avg_med[i] = 0
                ghi_max_med[i] = 0
                ghi_min_med[i] = 0

    horas = np.arange(1, 25)

    plt.figure(num_figura, figsize=(11, 8))
    plt.plot(ghi_avg_med, 'o-', color=cor3, linewidth=2.5, markerfacecolor=cor3, markersize=10, label='GHI avg')
    plt.plot(ghi_max_med, 'o-', color=cor1, linewidth=2.5, markerfacecolor=cor1, markersize=10, label='GHI max')
    plt.plot(ghi_min_med, 'o-', color=cor2, linewidth=2.5, markerfacecolor=cor2, markersize=10, label='GHI min')
    plt.grid(True, which='both', axis='both')
    plt.ylim([0, 1000])
    plt.xlim([1, 24])
    plt.xticks(horas)
    plt.xlabel('Hour', fontsize=18, fontname='Arial Narrow')
    plt.ylabel('[W/m²]', fontsize=18, fontname='Arial Narrow')
    plt.legend(loc='best')
    plt.title('Hourly Average Global Horizontal Irradiance', fontsize=20)
    plt.savefig(f'{nome_arquivo}_Average_Global_Horizontal_Irradiance.png', format='png', dpi=300)
    plt.savefig(f'{nome_arquivo}_Average_Global_Horizontal_Irradiance.pdf', format='pdf')

    # Plotting the total potential as a bar chart
    plt.figure(num_figura + 1, figsize=(3, 6))
    potencial = np.sum(ghi_avg_med) / 1000  # [kW/m²day]
    plt.bar(1, potencial, color=cor3)
    plt.grid(True)
    plt.ylim([0, 8])
    plt.yticks(np.arange(0, 9, 1))
    plt.xticks([1], [mes])
    plt.text(1, potencial, f'{potencial:.2f}', ha='center', va='bottom', fontsize=18)
    plt.ylabel('[kW/m²day]', fontsize=18, fontname='Arial Narrow')
    plt.title(nome_arquivo, fontsize=20)
    plt.savefig(f'{nome_arquivo}_Monthly_Average_Global_Horizontal_Irradiation.png', format='png', dpi=300)
    plt.savefig(f'{nome_arquivo}_Monthly_Average_Global_Horizontal_Irradiation.pdf', format='pdf')

    #plt.show()
