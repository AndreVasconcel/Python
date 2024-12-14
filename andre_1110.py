n=1

while n!=0:
    n = int(input())
    
    if n == 0:
        break

    pilha = list(range(1, n+1))
    descartados = []

    while len(pilha) > 1:
        descartados.append(pilha.pop(0))
        pilha.append(pilha.pop(0))
    
    if descartados:
        descartados_str = ""
        for i, card in enumerate(descartados):
            descartados_str += str(card)
            if i < len(descartados) - 1:
             descartados_str += ", "

        print(f"Discarded cards: {descartados_str}")

    else:
        print("Discarded cards:")
    
    print(f"Remaining card: {pilha[0]}")

