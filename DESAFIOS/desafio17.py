import math
catop = int(input('Digite o cateto oposto: '))
catad = int(input('Digite o cateto adjacente: '))
soma = pow(catop, 2)+pow(catad, 2)
hipo = (math.sqrt(soma))
print('A hipotenuza é:', hipo)
