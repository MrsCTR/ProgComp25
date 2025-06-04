'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
   
   MDC1 = int(input('informe um MDC1:'))
   MDC2 = int(input('informe um MDC2:'))

   if MDC1 <= 0 or MDC2 <= 0:
       sys.exit('ERRO: Informe um número inteiro positivo...')

   for _ in range(MDC2):
      resto = MDC1 % MDC2
      MDC1 = MDC2
      MDC2 = resto
      if MDC2 == 0:
         break
      print(f'O MDC é {MDC1}')

except ValueError:
   sys.exit('ERRO: Não foi informado um MDC válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
