'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''

import sys
import random

try:
    intNumero = int(input('\nInforme um valor para intNumero: '))
    intPosicao = int(input('Informe um valor para intPosicao: '))
except ValueError:
    sys.exit('\nERRO: Informe um valor inteiro válido para intNumero ou intPosicao...\n')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}...\n')
else:
    if intNumero <= 0 or intNumero > 100:
        sys.exit('ERRO: Informe um valor entre 1 e 100... \n')



listaValores = list()

for _ in range(intNumero):
    intvalor = random.randint(-100, 100)
    listaValores.append(intvalor)

print(listaValores)

lista_pares = list()

for intvalor in listaValores:
    if intvalor % 2 == 0:
        lista_pares.append(intvalor)

print(lista_pares)
