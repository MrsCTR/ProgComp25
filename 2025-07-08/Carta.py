import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}\\Carta.txt', 'r')

except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')
except Exception as erro:
    print(f'Erro:{erro}!')

else:
    strConteudo = arqLeitura.readlines()
    arqLeitura.close()
    print(strConteudo)