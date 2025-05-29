'''
Dado que um número primo é um número que só possui dois divisores (1 e ele mesmo),
faça um programa que solicite ao usuário um número inteiro e informe se ele é primo ou não.
'''
import sys
try:
      intValor = int(input('Informe um número positivo: '))
except ValueError:
      sys.exit('ERRO: Valor Inteiro Inválido...')
except Exception as e:
      sys.exit(f'ERRO: {e}')
else:
      intCntDivisor = 1
      intDivisor = 2

      while intDivisor <= intValor:
        if intValor % intDivisor == 0:
               intCntDivisor += 1
        intDivisor += 1

if intCntDivisor == 2:
      print('Primo')

else:
      print('Não primo')