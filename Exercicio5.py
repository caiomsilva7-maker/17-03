import os
os.system('cls')

soma = 0
QUANTIDADE_DE_NOTAS = 3

for i in range(QUANTIDADE_DE_NOTAS):
    nota = int(input('Digite a nota do aluno: '))
    soma += nota
media = soma / QUANTIDADE_DE_NOTAS
print(f"média: {media}")