distancia = int(input("Qual a distancia: "))
chovendo = True

# variável para o bônus da chuva para evitar repetir código
adicional_chuva = 2 if chovendo else 0

match distancia:
    case d if d < 5:
        taxa = 5 + adicional_chuva
        print("A taxa e:", taxa)

    case d if 5 <= d < 10:
        taxa = 8 + adicional_chuva
        print("A taxa e:", taxa)
    
    case d if d >= 10:
        taxa = 10 + adicional_chuva
        print("A taxa e:", taxa)
    
    case _:
        print("Distancia invalida.")
