'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''

import sys
import random
import math


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

    Contador = 1
    while Contador <= intNumero :
        intValor = random.randint(0, 1000)

        if intValor not in listaValores:
            listaValores.append(intValor)
            Contador += 1

print(listaValores)