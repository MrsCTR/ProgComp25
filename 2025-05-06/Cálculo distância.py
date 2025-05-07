import sys

velocidade = int (input ('digite o valor da velocidade inicial'))
if velocidade <=0: 
   sys. exit ('informe velocidade positiva')

Aceleração = int (input ('digite o valor da aceleração')) 
if Aceleração <=0: 
   sys. exit ('informe aceleração positiva')

Tempo = int (input('digite o valor do tempo'))
if Tempo <=0:
   sys. exit ('informe tempo positivo')

Distancia = v0 * t + (a * (t**2)) /2 # type: ignore

print (f'A distância percorrida é: {Distancia}')