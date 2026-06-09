M = int(input("idade da mãe: "))
A = int(input("idade filho 1: "))
B = int(input("idade filho 2: "))

# Calcula a idade do terceiro filho
C = M - (A + B)
print("terceiro filo tem idade", C)

mais_velho = max(A, B, C)
print("o filho mais velho tem", mais_velho,"anos")
