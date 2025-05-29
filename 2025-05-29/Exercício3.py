import sys

try:
    intvalor = int(input('...'))

except ValueError:
    sys.exit('...')
except Exception as e:
    sys.exit('...')

else:
    if intvalor <0:
        print('Não existe fatorial')
    elif intvalor <2:
        print(f'{intvalor} != 1')
        else:
        intfatorial = intvalor
        intaux = intvalor

while intaux <= 2:
    intaux -= 1
    intfatorial *= intaux

print(f'{intvalor} != {intfatorial} ')