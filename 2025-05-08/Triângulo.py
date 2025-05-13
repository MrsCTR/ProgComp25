'''
   Programa para classificar um triângulo quanto aos ângulos.

   - O programa deverá solicitar 3 ângulos inteiros positivos;
   - Para ser um triângulo, a soma dos ângulos deve ser igual a 180;

   - Retângulo: Possui um ângulointerno reto (igual a 90).
   - Obstusângulo: Possui um ângulo interno obtuso (maior que 90).
   - Acutângulo: Possui todos os ângulos internos agudos (menores que 90).
'''
import sys

# Solicitar os 3 ângulos do triângulo
ÂnguloA = int(input('digite o ângulo A: '))
ÂnguloB = int(input('digite o ângulo B: '))
ÂnguloC = int(input('digite o ângulo C: '))

# Verificando se os ângulos são positivos
if (ÂnguloA <=0) or (ÂnguloB <=0) or (ÂnguloC <=0):
    sys.exit('erro: um ou mais ângulos não são positivos.')

# verificar se a soma dos ângulos é igual a 180
if ÂnguloA + ÂnguloB + ÂnguloC !=180:
    sys.exit
