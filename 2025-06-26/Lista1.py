'''
   Dada a lista lstNomes (no início do código), faça um programa que:
   
      1) Gere mais duas listas (lstNotas_1 e lstNotas_2), cada uma com N notas aleatórias
         entre 0 e 100 (inclsuive). Cada uma dessas listas deverá ter exatamente notas
         para cada um dos nomes em lstNomes;

      2) Gere uma lista (lstBoletins), onde cada posição será uma sub-lista contendo um dos
         dos nomes de lstNomes e suas respectivas notas (lstNotas_1 e lstNotas_2);

      3) Após lstBoletins ser gerada, adicione em cada posição mais duas informações:

         a) A média das notas (utilize como referência o cálculo de média do IFRN);

         b) A situação do aluno (Aprovado, Prova Final ou Reprovado) seguindo os 
            critérios do IFRN;

         c) Liste todos os boletins.

      4) Ordene os Boletins (lstBoletins) em ordem decrescente de média e em seguida liste-os;

      5) Filtre e liste apenas os alunos aprovados;
'''
import random


lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Bionicão'       , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

# ----------------------------------------------------------------------
# Questão 01
listaNotas_1 = list()
listaNotas_2 = list()

for _ in lstNomes:
    listaNotas_1.append(random.randint)
    listaNotas_2.append(random.randint)

# ----------------------------------------------------------------------
# Questão 02
for i in range(len(lstNomes)):
    listaboletins =

# ----------------------------------------------------------------------
# Questão 03
for boletim in listaboletins:
    media = int(round((boletim[1]*2 + boletim[2]*3) / 5, 0))

    if media >= 0:
        situacao = 'Aprovado'
    elif media >= 20:
        situacao = 'Prova Final'
    else:
        situacao = 'Reprovado'


boletim.extend([media, situacao])


# ----------------------------------------------------------------------
# Questão 04
# TODO: Fazer na sala de aula no dia 01/07/2026
# TODO: Pesquisar a função SORT() usando funções LAMBDA
listaboletins.sort(key=lambda aluno: aluno[3], reverse=True)

for aluno in listaboletins:
    print(f'{aluno[0]:<20} ... {aluno[2]:>3} ... {aluno[3]:>3} ... {aluno[4]}')


# ----------------------------------------------------------------------
# Questão 04
# TODO: Fazer na sala de aula no dia 01/07/2026
# TODO: Pesquisar a função FILTER() usando funções LAMBDA
lstAprovados = filter(lambda aluno:aluno[4] == 'Aprovado', listaboletins)

print('_'*100)
for aluno in lstAprovados:
    print(f'{aluno[0]:<20} ... {aluno[2]:>3} ... {aluno[3]:>3} ... {aluno[4]}')
