alfabeto = "abcdefghijklmnopqrstuvwxyz"

string = input()
palavra = input()
new_pal = ""

for i in range(len(palavra)):
    for k in range(len(string)):
        if palavra[i] == string[k]:
            new_pal+=alfabeto[k]

print(new_pal)