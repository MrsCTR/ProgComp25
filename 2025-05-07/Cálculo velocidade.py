import sys

distância = int (input (100 km))
if distância <=0:
  sys.exit ('informe distância positiva')

v-inicial = int (input('30 km/h'))
if v-inicial <=0:
   sys.exit ('informe velocidade positiva')

acelera = int (input('10 m/s'))
if acelera <=0:
   sys.exit ('informe aceleração positiva')

distância *= 1000

v-inicial /= 3.6

delta = v_inicial ** 2 - 4 * acelera * distancia
if delta <0:
   sys.exit ('não é possível calcular o tempo')

t = ( -v_inicial + delta ** 0.5) / (2 * acelera)