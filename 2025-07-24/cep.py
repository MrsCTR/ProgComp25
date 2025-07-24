import requests, sys

strCEP = input('Informe o CEP: ')

try:
    reqHTTP = requests.get('https://viacep.com.br/ws/{strCEP}/json')
except Exception as erro:
    sys.exit(f'Erro: {erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('Erro na Requisição')
    
    dictCartola = reqHTTP.json()
    print(dictCartola)