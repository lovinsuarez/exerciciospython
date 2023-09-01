from random import randint
from time import sleep
computador = randint (0, 5)
print('-=-' * 10)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS VC CONSEGUIU ME VENCER')
else:
    print('eu pensei no número {} e não no número {}!'.format(computador, jogador))
