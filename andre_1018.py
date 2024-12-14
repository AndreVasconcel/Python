cedulas = [100, 50, 20, 10, 5, 2, 1]

N = int(input())

quant = 0
new_N = 0

print(N)

for i in cedulas:
    quant = N/i
    new_N = N-(quant*i)
    formato = int(quant)
    print(f"{formato} nota(s) de R$ {i},00")
    N = N-(formato*i)
