'''
Programa que solicite ao usuário números inteiros
aleatoriamente até que seja informado o valor 0

Quando for digitado o valor 0, o programa deverá informar:
a) Quantos números inteiros foram digitados;
b) A soma dos números inteiros positivos;
c) A média dos números inteiros positivos;

O valor 0 digitado não deve ser considerado em nenhum dos itens acima.
'''

intvalor          = None
intsomapositivos  = 0
intqtvalores      = 0
intqtvalpositivos = 0


while intvalor != 0:
    try:
        intvalor = int(input('Informe um valor inteiro: '))
    except ValueError:
      print('ERRO: Valor inteiro inválido...')
    except Exception as e:
      print(f'ERRO: {e}')
else:
    if intvalor > 0: 
       intsomapositivos += intvalor
       intqtvalpositivos += 1

    if intvalor != 0:
      intqtvalores += 1

print(f'Quantos números inteiros foram digitados: {intqtvalores}')
print(f'Soma dos números inteiros positivos.....: {intsomapositivos}')
print(f'Média dos números inteiros positivos....: {intsomapositivos / intqtvalpositivos}')