import math
num = float(input('Insira um valor em graus: '))
c = math.ceil(math.cos(num))
s = math.ceil(math.sin(num))
t = math.ceil(math.tan(num))
print('O coseno é: {}\nO seno é: {}\nA tangente é: {}'.format(c, s, t))
