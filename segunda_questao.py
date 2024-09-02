def verificar_letra_a(text:str):
    check = False
    count = 0
    for i in text:
        i = i.lower()
        if i == "a":
            count += 1
            check = True
    
    return check, count

palavra = input("Digite a sua palavra: ")

verificar, qtd = verificar_letra_a(palavra)

if verificar:
    print(f"Temo a ocorrência de {qtd} vezes da letra 'A' na palavra {palavra}.")
else:
    print(f"Não temos a ocorrência da letra 'A' na palavra {palavra}")
