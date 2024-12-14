#Critérios
#1 - SIM
#2 Quantidade de letras do primeiro nome
#3 - SE EMPATE, ENTÃO O QUE SE INSCREVEU PRIMEIRO
# Imprimir em ordem alfabética

entrada = ""
y = " YES"
n = " NO"
lista_yes = []
lista_no = []

while entrada!="FIM":
    entrada = input()

    if "YES" in entrada:
        entrada_sem_palavra = entrada.replace(y, "")
        if entrada_sem_palavra not in lista_yes:
            lista_yes.append(entrada_sem_palavra)
    elif "NO" in entrada:
        entrada_sem_palavra = entrada.replace(n, "")
        if entrada_sem_palavra not in lista_no:
            lista_no.append(entrada_sem_palavra)
    
    amigo_do_habay = ""
    for candidato in lista_yes:
        if len(candidato)>len(amigo_do_habay):
            amigo_do_habay = candidato
    
lista_no.sort()
lista_yes.sort()

for i in lista_yes:
    print(i)
    
for k in lista_no:
    print(k)

print("\nAmigo do Habay:\n" + amigo_do_habay)