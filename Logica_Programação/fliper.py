P, R = map(int, input("digite as duas posições para P e R :").split())

if P == 0:
    print("porta C")
elif P == 1 and R ==1 :
    print("porta A")
else:
    print("porta B")