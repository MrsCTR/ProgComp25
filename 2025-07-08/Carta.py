import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}//Carta.txt', 'r', encoding= 'utf-8')

except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')
except Exception as erro:
    print(f'Erro:{erro}!')

else:
    strConteudo = arqLeitura.read()
    arqLeitura.close()
    print(strConteudo)