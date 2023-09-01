valor = float(input('Qual é o preço do produto? R$:'))
por = valor - (valor*5/100)
print('o valor do produto {:.2f} com desconto de 5% é {:.2f}.'.format(valor, por))
