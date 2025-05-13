import sys

try:
    intdividendo = int(input('digite o dividendo: '))
    intdivisor = int(input('digite o divisor..: '))
    fltresultado = intdividendo / intdivisor
except ValueError:
    print('erro: informe um valor que possa ser convertido em inteiro.')
except ZeroDivisionError:
    print('erro: não existe divisão por zero')
except:
    print(f'erro: {sys.exc_info()}')
else:
    print(fltresultado)