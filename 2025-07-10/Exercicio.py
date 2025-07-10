'''
   Fazer um programa que faça as seguintes operações.

   1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      

   2) Gerar arquivos para cada ano. Salvar o arquivo com o mesmo nome do arquivo que 
      foi aberto na questão 1, adionando no final do nome o sufixo "_nnnn" onde "nnnn" 
      corresponde ao ano das cotações;


   3) Gerar arquivos por ano com as médias das cotações mensais. Salve os arquivos com 
      o nome "media_cotacao_nnnn.csv" onde "nnnn" corresponde ao ano. Cada linha do arquivo
      deverá ter o nome do mês e em seguida o valor médio da cotação. Separe os valores da 
      linha por ";";
'''

import os
from datetime import datetime

strDir = os.path.dirname(__file__)

try:
   
   arqLeitura = open(f'{strDir}\\cotacao_dolar.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   print('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   print(f'\nERRO: {erro}')
else:
   lstCotacao = []
   lstCabecalho = arqLeitura.readline().strip().split(';')

   while True:
      strLinha = arqLeitura.readline().strip()   
      # Interrompe o laço quando não há conteúdo na linha (EOF)
      if not strLinha:
        break
      Valores = strLinha.split(';')

try:
    cotacao_compra = float(Valores[0])
    cotacao_venda = float(Valores[1])
    dh_cotacao = datetime.strptime(Valores[2], '%d-%m-%Y')
    lstCotacao.append([cotacao_compra, cotacao_venda, dh_cotacao])

except (ValueError, IndexError) as e:
   print(f"Erro ao processar a linha: '{strLinha}'. Detalhes: {e}. Esta linha será ignorada.")

arqLeitura.close()

for item in lstCotacao:
        print(item)