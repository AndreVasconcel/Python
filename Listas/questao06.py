def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

def soma_fatorial(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += fatorial(i)
    return soma

# Exemplo de uso da função
numero = int(input("Número: "))
resultado = soma_fatorial(numero)
print(f"A soma dos fatoriais de 1 até {numero} é:", resultado)