import os, sys

strDir = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{strDir}//times_header.csv', 'r', encoding= 'utf-8')

except FileNotFoundError:
    sys.exit('Erro: Arquivo não encontrado!')
except Exception as erro:
    sys.exit(f'Erro:{erro}!')

else:

    lstTimes = list()
    lstcabecalho = arqLeitura.readline().strip().split(';')

    while True:
       strLinha = arqLeitura.readline().strip()
       if not strLinha: break
       lstAux = [int(i) if i.isdigit() else i for i in strLinha.split(';')]
       lstTimes.append(lstAux)
    arqLeitura.close()

for time in lstTimes:
    time.insert(4, time[1]*3 + time[2])
    time.append(time[5] - time[6])

lstcabecalho.insert(4, 'pontuação')
lstcabecalho.append('Saldo de Gols')

lstTimes.sort(key=lambda time: (time[4], time[1], time[7], time[5]), reverse=True)

print(lstcabecalho)
for time in lstTimes:
    print(time)