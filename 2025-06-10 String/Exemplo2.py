'''Add commentMore actions
   Programa para ao digitar uma palavra ela seja escrita da seguinte forma 
   (como exemplo iremos usar a palavra PROGRAMAÇÃO).

   p
   PR
   PRO
   PROG
   ...
   PROGRAMAÇÃO  
'''

strTexto = input('Digite um texto: ')
Posicao = 1

while Posicao <= len(strTexto):
   print(strTexto[0:Posicao + 1])
   Posicao += 1
