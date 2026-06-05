n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
n3 = int(input("digite outro numero: "))

if n1>n2 and n1>n3:
    print(n1,"e o maior")
elif n2>n1 and n2>n3:
    print(n2,"e o maior")
else:
    print(n3,"e o maior")