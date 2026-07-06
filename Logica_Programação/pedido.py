hamburguer = int(input("Quantidade de hambúrgueres: "))
batata = int(input("Quantidade de batatas fritas: "))
refrigerante = int(input("Quantidade de refrigerantes: "))

total = (hamburguer * 12) + (batata * 7) + (refrigerante * 5)

print(f"Valor total do pedido: R$ {total:.2f}")