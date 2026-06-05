x = int(input("um numero: "))
y = int(input("outro numero: "))

if x > 0 and y > 0: #ambos positivos
    print("primeiro quadrante")
elif x < 0 and y > 0:
    print("segundo quadrante")
elif x < 0 and y < 0:
    print("terceiro quadrante")
elif x > 0 and y < 0:
    print("quarto quadrante") 
else: 
    print("eixo")#ambos 0