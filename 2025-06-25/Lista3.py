'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista onde cada posição será 
         uma sub-lista com 3 posições:

         a) A primeira posição será o número anterior ao número da lista inicial;
         b) A segunda posição será o número da lista inicial; 
         c) A terceira posição será o número seguinte ao número da lista inicial.
'''
import sys
import random


try:
    intNumero = int(input('\nInforme um valor para intNumero: '))
except ValueError:
    sys.exit('\nERRO: Informe um valor inteiro válido para intNumero ou intPosicao...\n')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}...\n')
else:
    if intNumero <= 0 or intNumero > 100:
        sys.exit('ERRO: Informe um valor entre 1 e 100... \n')



    listaValores = list()
    listaTrios = list()

    for _ in range(intNumero):
        intValor = random.randint(-100, +100)

        listaValores.append(intValor)
        listaTrios.append([intValor-1, intValor, intValor+1])

    print(listaValores)    
    print(listaTrios)