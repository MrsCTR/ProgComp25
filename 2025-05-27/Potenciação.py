'''
Programa para executar uma potenciação de 2 números inteiros utilizando apenas o operador produto (*)
'''
import sys

try:
    
    intbase = int(input('informe a base... '))
    intpotencia = int(input('Informe a potencia... '))
except ValueError:
    sys.exit('ERRO: Não foi informado um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    if intbase <= 0:
        sys.exit('ERRO: Informe uma base positiva...')

    if intpotencia <= 0:
        sys.exit('ERRO: Informe uma potencia positiva...')

    intpotenciacao = 1
    Contador = 1
    while Contador <= intpotencia:
        intpotenciacao *= intbase
        Contador += 1

    print(f'{intbase} ** {intpotencia} = {Contador}')