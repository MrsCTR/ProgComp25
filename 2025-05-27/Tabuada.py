'''
   Programa para exibir a tabuada de multiplicação de
   um determinado número inteiro positivo
'''

import sys
try:
   intMultiplicador = int(input('Informe o Multiplicador: '))  

   if intMultiplicador <= 0 or intMultiplicador > 10:
         sys.exit('ERRO: Informe um valor inteiro positivo e que não seja maior que 10...')

   intMultiplicando = 1
   while intMultiplicando <= 10:
      print(f'{intMultiplicador} x  {intMultiplicando} = {intMultiplicador * intMultiplicando}')
      intMultiplicando += 1
   

   for intMultiplicando in range(1, 11, 1):
       print('FIM DA TABUADA...')
except ValueError:
   sys.exit('ERRO: Informe um valor inteiro...')
except Exception as e:
   sys.exit(f'ERRO {e}')