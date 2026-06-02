nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))

media = (nota1 + nota2)/ 2
print("sua media final e: ",media)

if media >= 7:
    print("vc foi aprovado")
elif media >= 4:
    print("vc esta de recuperação")
else:
    print("vc esta reprovado")