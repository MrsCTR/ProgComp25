'''
   Programa para verificar quantas vogais existem em uma string informada pelo usuário.Add commentMore actions
'''
strTexto = input('Digite um texto: ').upper()
strVogais = 'AEIOUÂÊÎÔÛÃÕÁÉÍÓÚ'
Vogais = 0


for strLetra in strTexto:
    if strLetra in strVogais:
        Vogais += 1

        print(f'Otexto possui {Vogais} vogais')