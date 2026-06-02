DDD = int(input("digite o numero do seu DDD para discagem: "))

match DDD:
    case 61:
        print("DDD de Brasilia")
    case 71:
        print("DDD de Salvador")
    case 11:
        print("DDD de São Paulo")
    case 21:
        print("DDD do Rio de Janeiro")
    case 32:
        print("DDD de Juiz de Fora")
    case 19:
        print("DDD Campinas")
    case 27:
        print("DDD Vitoria")
    case 31:
        print("DDD Belo Horizonte")
    case _:
        print("DDD não cadastrado")