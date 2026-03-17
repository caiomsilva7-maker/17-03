import os
os.system('cls')
import time

a = int(input('Digite o número: '))
b = int(input('Digite o número: '))
c = int(input('Digite o número: '))

média = (a + b + c) / 3 
if média >= 7:
    print('Aprovado')   
elif média <= 4:
    print('Reprovado')  