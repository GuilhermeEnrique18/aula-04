somaNegativos = 0
for i in range(1,11,1):
    N = int(input(f"Digite 10 números, digite N{i}: "))
    if N <0:
        somaNegativos+=1
print(somaNegativos)