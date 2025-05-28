'''
Programa para executar um produto de 2 números inteiros positivos utilizando apenas o operador soma (+)
'''
import sys

try:
    
    intmultiplicador = int(input('Informe o primeiro numero inteiro positivo (Multiplicador): '))
    intmultiplicando = int(input('Informe o segundo numero inteiro positivo (Multiplicando): '))
except ValueError:
    sys.exit('ERRO: Não foi informado um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    if intmultiplicador <= 0:
        sys.exit('ERRO: Informe multiplicador positivo...')

    if intmultiplicando <= 0:
        sys.exit('ERRO: Informe multiplicando positivo...')

    intproduto = 0
    Contador = 1
    while Contador <= intmultiplicando:
        intproduto += intmultiplicando
        Contador += 1

    print(f'{intmultiplicador} x {intmultiplicando} = {intproduto}')
