import pandas as pd
from testes.teste_limites_fisicos import teste_limites_fisicos
from testes.teste_bsrn import teste_bsrn
df = pd.read_excel('data/SPES01-2024-09.xlsx', skiprows=1443)


var_avg = df.iloc[:,32]
#print(var_avg[:5])
n = var_avg.shape[0]

lf_dhi, lf_dhi_flag = teste_limites_fisicos(var_avg, var_avg, 2000, -5, n)

fpmin = -4
fpmaxdhi = (0.95 * iox * cosAZS12) + 50
ermin = -2
ermaxdhi = (0.75 * iox * cosAZS12) + 30

#print(f"Teste aplicado Fisicamente Possível: lf_ghi1: {lf_ghi1} e {lf_ghi_flag}")
bsrn_dhi, bsnr_dhi_flag = teste_bsrn(lf_dhi, var_avg, fpmin, fpmaxdhi, ermin, ermaxdhi, n)

print(lf_dhi_flag.astype(int))