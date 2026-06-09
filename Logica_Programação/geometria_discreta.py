#descobrir a quantidades de lajotas tipo 1 e 2 para a area de uma sala
L = int(input("largura: "))
C = int(input("comprimento: "))

# Aplicação das fórmulas de contagem de lajotas
tipo_1 = (L * C) + ((L - 1) * (C - 1))
tipo_2 = 2 * (L - 1) + 2 * (C - 1)

print(tipo_1)
print(tipo_2)
