import os 
os.system('cls')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

s = n1 + n2 + n3
m = s / 3

if m >= 7:
    print('Aprovado')
elif m <= 4:
    print('Reprovado')