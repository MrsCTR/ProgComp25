# Solicita o número para calcular

import sys
try:
    multiplicador = int(input('Digite o multiplicador da tabuada: '))
except ValueError:
    sys.exit('erro:informe um valor inteiro.')
else:
    if multiplicador <= 1

multiplicando = 1
while multiplicando <= 10:
    print(f'{multiplicador} x {multiplicando} = {multiplicador} * {multiplicando}')
    multiplicando += 1

print('fim da tabuada...')