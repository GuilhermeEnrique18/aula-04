somaNotas = 0
N = int(input())
for i in range (1,5):
    notas = int(input(f"informe o numero {i}: "))
    somaNotas = somaNotas + notas
media = somaNotas / 5
print(f"Sua media foi: {media}")