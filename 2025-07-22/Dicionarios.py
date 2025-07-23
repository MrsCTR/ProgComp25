import os, sys, json

strDirApp = os.path.dirname(__file__)

strNomeArq = f'{strDirApp}//cartola_fc_2024.json'

try:
    arqInput = open(strNomeArq, 'r', encoding='utf-8')
    strDados = arqInput.read()
    dictCartola = json.loads(strDados)
    arqInput.close()

except FileNotFoundError:
    sys.exit('Erro: Arquivo não existe...')
except json.JSONDecodeError:
    sys.exit('Erro: O conteúdo do arquivo não está no formato correto')
except Exception as erro:
    sys.exit(f'Erro: {erro}...')
else:
    #lstChaves = list(dictCartola.keys()) # ['clubes', 'posicoes', 'status', 'atletas']
    
    
    '''
    dictCartola = { 'clubes': {...}, 'posicoes': {...}, 'status': {...}, 'atletas': [...]

    dictCartola['clubes']    -> dicionário (k:v)
    dictCartola['posicoes']  -> dicionário (k:v)
    dictCartola['status']    -> dicionário (k:v)
    dictCartola['atletas']   -> lista (indice -> dicionário (k:v)
    '''

# Informando o nome do clube    
strClube = input('Informe o nome do clube: ').strip().lower()

# Obtendo o ID do clube informado



for cartola_fc_2024 in strClube.split():
    if strClube in cartola_fc_2024.keys():
      dictCartola['clubes']

# Listando os atletas do clube informado
lstAux = dictCartola['atletas']
#clube_id = ['clube_atleta']

   