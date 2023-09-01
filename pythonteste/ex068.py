from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar[P/I]?')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador jogou {computador} e o total é de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Parabéns Você ganhou!!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Parabéns Você ganhou!!!!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')

