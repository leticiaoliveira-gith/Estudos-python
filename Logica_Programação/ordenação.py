n1 = int(input("digite um numero: "))
n2 = int (input("digite outro numero: "))
n3 = int (input("digite outro numero: "))

numeros = [n1,n2,n3]

numeros_ordenado = sorted(numeros)

for numeros in numeros_ordenado:
    print(numeros)