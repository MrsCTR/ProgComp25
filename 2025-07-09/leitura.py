import os

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}//times.csv', 'r', encoding= 'utf-8')

except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')
except Exception as erro:
    print(f'Erro:{erro}!')

else:

    lstTimes = list()

    while True:
       strLinha = arqLeitura.readline().strip()
       if not strLinha: break
       lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]
       lstTimes.append(lstAux)
    arqLeitura.close()


print(lstTimes)