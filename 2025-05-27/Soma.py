'''
Programa para executar um produto de 2 números inteiros positivos utilizando apenas o operador soma (+)
'''
import sys

try:
    
    numero1 = int(input('Informe o primeiro numero inteiro positivo (Multiplicador): '))
    numero2 = int(input('Informe o segundo numero inteiro positivo (Multiplicando): '))

    if numero1 <= 0 or numero2 <= 0:
        sys.exit('ERRO: Os numeros devem ser inteiro positivo.')

    Resultado = 0
    Contador = 0
    Expressão = " "

    while Contador < numero2:
        Resultado += numero1
        Expressão += f'{numero1} + ' if Contador < numero2 - 1 else f"numero1"
        
        print(f'{Expressão} total {Resultado}')
        Contador += 1
except ValueError:
    sys.exit('ERRO: Por favor, valores inteiros válidos.')
except Exception as e:
    sys.exit(f'ERRO: {e}')