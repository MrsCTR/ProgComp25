import sys, Funcoes

try:
    E1 = int(input('Informe E1:'))
    E2 = int(input('Informe E2:'))

except ValueError:
    sys.exit('Informe inteiro válido')
except Exception as erro:
    sys.exit(f'Erro: {erro}')
else:
    try:
        MediaFinal = Funcoes.mediaIFRN(E1, E2)
    except Exception as erro:
        print(erro)
    else:
        print(f'Média = {MediaFinal}')
