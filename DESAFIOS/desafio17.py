import math
catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente: '))
hi = math.hypot(catop, catad)
#soma = pow(catop, 2)+pow(catad, 2)
#hipo = (math.sqrt(soma))
print('A hipotenuza é: {: .2f}' .format(hi))
