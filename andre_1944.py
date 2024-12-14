N = int(input())
painel = ['F', 'A', 'C', 'E']
brindes = 0

while N > 0:
    palavra = input()
    fila = palavra.split()

    if fila == painel[-4:][::-1]:
        brindes += 1
        painel = painel[:-4]
        if not painel:
            painel = ['F', 'A', 'C', 'E']
    else:
        painel += fila

    N -= 1

print(brindes)