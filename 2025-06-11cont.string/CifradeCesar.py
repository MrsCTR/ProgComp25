'''
   A cifra de César pode ser aplicada não apenas a letras, mas a todos os caracteres 
   de uma mensagem, deslocando o código Unicode de cada caractere por um valor fixo.

   Escreva um programa em Python que:

      a) Solicite ao usuário uma mensagem de texto 
         (qualquer caractere, incluindo letras, números, símbolos, espaços e pontuação);

      b) Solicite ao usuário  um número inteiro que será o deslocamento da cifra;

      c) Para cada caractere da mensagem, converta seu código Unicode (usando a função ORD), 
         some o deslocamento e depois converta de volta para caractere (usando CHR).

      d) Exiba a mensagem cifrada resultante.

   EXEMPLO: 
      Digite a Mensagem .....: Olá, Mundo 2025!
      Informe o Deslocamento : 6
      Mensagem cifrada ......: Uré2*'Sútsj&868;'
'''
import sys

try:
    
    strMensagem = input('Digite a mensagem...:')
    Deslocamento_Cifra = int(input("informe o Deslocamento_Cifra:"))
except ValueError:
   sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
   sys.exit(f'ERRO: {e}')
else:
    Mensagem_Cifrada = ''

for strLetra in strMensagem:
    
    Mensagem_Cifrada += chr(ord (strLetra) + Deslocamento_Cifra)
    
    print("Mensagem_Cifrada......:", Mensagem_Cifrada)