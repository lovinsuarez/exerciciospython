numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('valor duplicado...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'voce digitou os valores {numeros}')
