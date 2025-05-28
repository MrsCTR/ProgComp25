# Solicita o número para calcular

import sys

try:
   Multiplicador = int(input('Informe o Multiplicador: '))
except ValueError:
   sys.exit('ERRO: Informe um valor inteiro...')
except Exception as e:
   sys.exit(f'ERRO {e}')
else:  
   if Multiplicador <= 0:
      sys.exit('ERRO: Informe um valor inteiro positivo...')

   Multiplicando = 1
   while Multiplicando <= 10:
      print(f'{Multiplicador} x  {Multiplicando} = {Multiplicador * Multiplicando}')
      Multiplicando += 1

   print('FIM DA TABUADA...')