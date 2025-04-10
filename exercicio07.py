somaNotas = 0
N = int(input("informe a quantidade de números que você quer para calcular a media: "))
for i in range (1,N+1):
    notas = int(input(f"informe a nota {i}: "))
    somaNotas = somaNotas + notas
media = somaNotas / N
print(f"Sua media foi: {media:.2f}")