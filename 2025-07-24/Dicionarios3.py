import requests, sys

try:
    reqHTTP = requests.get('https://https://api.cartolafc.globo.com/atletas/mercado')

except Exception as erro:
    sys.exit(f'Erro: {erro}')
else:
    if reqHTTP.status_code != 200:
        sys.exit('Erro na Requisição')
    
    dictCartola = reqHTTP.json()
    print(dictCartola)