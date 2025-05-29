'''
Considerando que o fatorial de um número é dado por:
n!= n * (n-1) * (n-2) * (n-3) * ... * 1
Faça um programa que solicite um valor inteiro ao usuário,
em seguida calcule e exiba o fatorial do número informado.
'''

import sys


while intValor != 0:
   try:
      intValor = int(input('Informe um valor inteiro: '))
      sys.exit 
   except ValueError:
      print('ERRO: Valor Inteiro Inválido...')
   except Exception as e:
      print(f'ERRO: {e}')
   else:
      if intValor > 0:
         intSomaPositivos  += intValor
         intQtValPositivos += 1

      if intValor != 0:
         intQtValores += 1