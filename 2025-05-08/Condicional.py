import sys 

# Informe a nota da etapa 1
etapa1 = int(input('informe a nota da etapa 1: '))
if etapa1 < 0 or etapa1 >100:
   sys.exit('erro: Nota etapa 1 inválida. informe nota entre 0 e 100')

# Informe a nota da etapa 2
etapa2 = int(input('informe a nota da etapa 2: '))
if etapa2 < 0 or etapa2 >100:
   sys.exit('erro: Nota etapa 2 inválida. informe nota entre 0 e 100')


   # Calculando a média
media = int( round((etapa1 * 2 + etapa2 * 3) /5,0))
print(f'Média do aluno:{media}')#não aceita os quebrados
print(f'Media do aluno:{media:.0f}')#aceita os quebrados

#verificando a situação do aluno
if media >= 60:
    print('aluno aprovado.')
elif media >= 20:
    print('aluno prova final.')
else:
    print('aluno reprovado')