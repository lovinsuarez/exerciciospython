total = menor = totmil = cont = 0
barato = ''
print('LOJA DO LOVIN')
while True:
    produto = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o valor do produto? R$ '))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if cont == 'N':
        break
print('Acabou')
print(f'O valor total dos produtos é de {total:.2f}')
print(f'na sua compra tem {totmil} produtos a cima de R$ 1000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor}')
