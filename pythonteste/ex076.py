listagem = ('lapis', '1.75', 'borracha', '2', 'caderno', '15.20', 'estojo', '12,50')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7}')