'''
   A sequência de Fibonacci é uma sequência numérica onde cada número 
   é a soma dos dois anteriores, com os dois primeiros números sendo 1 e 1. 

   Implemente um programa que receba um número inteiro n e retorne os n 
   primeiros termos da sequência de Fibonacci.
'''
import sys

try:
   QuantidadeNumeros = int(input('Informe a quantidade de números da sequência'))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
    if QuantidadeNumeros < 2:
       sys.exit('Erro: a sequência de Fibonacci deve possuir pelo menos 2 números')

       NumeroAtual = 1
       ProximoNumero = 1
       print(f'{NumeroAtual}, {ProximoNumero},', end = '') 

if QuantidadeNumeros == 2:
   sys.exit('\n')

for _ in range(3, QuantidadeNumeros + 1):
   # Auxiliar = ProximoNumero
   # ProximoNumero = ProximoNumero + NumeroAtual
   # NumeroAtual = Auxiliar

   NumeroAtual, ProximoNumero = ProximoNumero, ProximoNumero
   print(f'{ProximoNumero},', end = '')

print('\n')
