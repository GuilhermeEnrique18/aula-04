somaIntervalo = 0
somaFora = 0

for i in range(10):
    N = int(input("Digite um número"))
    if N >9 and N <21:
        somaIntervalo+=1
somaFora= 10 - somaIntervalo
print(f"{somaIntervalo} estão dentro do intervalo e {somaFora} fora")