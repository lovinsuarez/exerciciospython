temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp [1]
        if temp [1] < men [1]:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in  'Nn':
        break
print(f'os dados foram {princ}')
print(f'Ao todo voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai} Kg')
print(f'O menor peso foi de {men} Kg')
