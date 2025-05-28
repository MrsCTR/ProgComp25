'''
Dada uma palavra chave, o programa só deve parar de pedir quando
o usuário digitar a palavra chave.
'''

strpalavrachave = '123Mudar'
strpalavrainfo = ''

while strpalavrainfo != strpalavrachave:
    strpalavrainfo = input('digite a palavra chave: ')

print('Você digitou a palavra chave...')