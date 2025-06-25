'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''

import sys
import random

try:
    intNumero = int(input('\nInforme um valor para intNumero: '))
    intPosicao = int(input('Informe um valor para intPosicao: '))
except ValueError:
    sys.exit('\nERRO: Informe um valor inteiro válido para intNumero ou intPosicao...\n')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}...\n')
else:
    if intNumero > 100 or intPosicao <= 0:
        print('ERRO: intNumero inválido (deve ser maior ou igual a 0) ou intPosicao fora do intervalo permitido (0 a 100).')

    try:
        tamanho_N = int(input('Informe o tamanho da lista (N, entre 1 e 100): '))
        if 1 <= tamanho_N <= 100:
            
        else:
            print('ERRO: O tamanho N deve ser um número inteiro entre 1 e 100.')
    except ValueError:
        sys.exit('\nERRO: Informe um valor inteiro válido para N.\n')
    except Exception as erro:
        sys.exit(f'\nERRO inesperado: {erro}\n')

VMinimo = -100
VMaximo = 100
lista_principal = [random.randint(VMinimo, VMaximo) for _ in range(tamanho_N)]

print(f'\nLista principal gerada ({tamanho_N} elementos):')
print(lista_principal)

lista_pares = [numero for numero in lista_principal if numero % 2 == 0]

print('\nLista com apenas os números pares:')
print(lista_pares)
