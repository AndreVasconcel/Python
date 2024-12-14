while True:
    n = int(input())

    if n == 0:
        break

    A = list(map(int, input().split()))

    A.sort()

    atual = (A[0], 1)
    res = atual[0]
    for i in range(1, n):
        if A[i] == atual[0]:
            atual = (atual[0], atual[1] + 1)
        else:
            if atual[1] % 2 == 1:
                res = atual[0]
                break
            else:
                atual = (A[i], 1)

    if atual[1] % 2 == 1:
        res = atual[0]

    print(res)