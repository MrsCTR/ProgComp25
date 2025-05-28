'''
Programa que solicite ao usuário números inteiros
aleatoriamente até que seja informado o valor 0

Quando for digitado o valor 0, o programa deverá informar:
a) Quantos números inteiros foram digitados;
b) A soma dos números inteiros positivos;
c) A média dos números inteiros positivos;

O valor 0 digitado não deve ser considerado em nenhum dos itens acima.
'''

intvalor = None
somapositivos = 0
quantvalpositivos = 0
quantvalores = 0

while intvalor != 0:
    try:
        intnumero = int(input('Informe um número inteiro positivo: '))
    except ValueError:
      print('ERRO: Informe um número inteiro válido...')
    except Exception as e:
      print(f'ERRO: {e}')
else:
    if intvalor > 0: 
       somapositivos += intvalor
       quantvalpositivos += 1

    if intvalor != 0:
      quantvalores += 1

print(f'quantidade dos números inteiros positivos...: {quantvalpositivos}')
print(f'soma dos números inteiros positivos...: {somapositivos}')
print(f'média dos números inteiros positivos...: {somapositivos/quantvalpositivos}')