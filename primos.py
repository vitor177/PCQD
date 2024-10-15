n = 200
for j in range(1, n):
    contador = 0
    for i in range(1, j+1):  # Verifica divisores de 1 até j
        if j % i == 0:
            contador += 1

    if contador == 2:  # Um número primo tem exatamente 2 divisores (1 e ele mesmo)
        print(f"{j} é primo")
