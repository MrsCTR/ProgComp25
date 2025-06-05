'''
   Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica 
   cujo quociente (q) ou razão entre um número e outro (exceto o primeiro) 
   é sempre igual. Vale lembrar que essa razão é sempre constante e pode 
   ser qualquer número racional (positivos, negativos, frações) exceto o 
   número zero (0).

   Faça um programa que:
      a) Solicite ao usuário um valor inteiro inicial e a razão da P.G.;
      b) Solicite um novo valor inteiro positivo correspondente a quantidade 
         de elementos da PG e exiba os valores dessa P.G.;
      c) Informe se a P.G. é constante, oscilante, crescente ou decrescente;
      d) Calcule a soma dos elementos dessa P.G.;
      e) Solicite um outro valor inteiro n correspondente a enésima posição 
         de um elemento da P.G. e exibir o valor desse elemento.
'''

import sys



try:
   Razao = int(input)
   QuantidadeElementos = int(input('Informe a quantidade de números da sequência'))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
   if Razao == 0:
      sys.exit('Erro: a razão deve ser diferente de zero')

   if QuantidadeElementos <= 0:
      sys.exit('Erro: a quantidade de elementos deve ser positiva')

ElementoPG = ValorInicial

print('\n elementos da P.G.')
print()