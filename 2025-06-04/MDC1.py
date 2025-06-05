'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
   
   MDC1 = int(input('informe um MDC1:'))
   MDC2 = int(input('informe um MDC2:'))
except ValueError:
   sys.exit('ERRO: Não foi informado um MDC válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
  
   if MDC1 <= 0 or MDC2 <= 0:
       sys.exit('ERRO: Informe um número inteiro positivo...')

   Auxiliar_MDC1 = MDC1
   Auxiliar_MDC2 = MDC2

   while Auxiliar_MDC2 !=0:
      Auxiliar_MDC1, Auxiliar_MDC2, Auxiliar_MDC1 % Auxiliar_MDC2

   print(f'MDC({MDC1}, {MDC2}) = {Auxiliar_MDC1}')
