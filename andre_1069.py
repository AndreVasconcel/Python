N = int(input())

for i in range(N):
    diamantes = 0
    cont=0
    l = input()

    for i in l:
        if i=="<":
            cont+=1
        elif i==">" and cont>=1:
            diamantes+=1
            cont-=1
    
    print(diamantes)
        