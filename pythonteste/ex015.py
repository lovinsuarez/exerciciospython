dias = int(input('Por quantos dias você alugou o carro?'))
KM = float(input('Quantos KM percorridos?'))
VD = dias * 60
KMP = KM * 0.15
print('Você alugou o carro por {} dias e percorreu {}KM e o valor total a pagar é de R${:.2f}. '.format(dias, KM,VD+KMP))
