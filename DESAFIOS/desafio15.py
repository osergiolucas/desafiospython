al=int(input('Quantos dias foi alugado? '))
d=float(input('Qual a distancia percorrida em Km? '))
p=float((60*al) + (d*0.15))
print('O preço a pagar pela locação do seu veículo é de R${:.2f}'.format(p))
