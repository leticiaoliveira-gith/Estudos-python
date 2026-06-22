t1 = int(input("Tempo do nadador 1: "))
t2 = int(input("Tempo do nadador 2: "))
t3 = int(input("Tempo do nadador 3: "))

# Lista de tuplas associando (tempo, número do nadador)
nadadores = [(t1, 1), (t2, 2), (t3, 3)]
nadadores.sort()


print(f"Ouro: Nadador {nadadores[0][1]} (Tempo: {nadadores[0][0]})")
print(f"Prata: Nadador {nadadores[1][1]} (Tempo: {nadadores[1][0]})")
print(f"Bronze: Nadador {nadadores[2][1]} (Tempo: {nadadores[2][0]})")
