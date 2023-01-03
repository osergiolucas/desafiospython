import math
num = float(input('Insira um valor em graus: '))
seno = math.sin(math.radians(num))
print('o angulo de {} tem o seno de {:.2f}'.format(num, seno))
co = math.cos(math.radians(num))
print('o angulo de {} tem o cosseno de {:.2f}'.format(num, co))
ta = math.tan(math.radians(num))
print('o angulo de {} tem a tangente de {:.2f}'.format(num, ta))
