def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [int(input('Valor 1: ')), int(input('Valor 2: ')), int(input('Valor 3: '))]
dobra(valores)
print(f'A multiplicação do valor 1 é {len(valores[0])} 2 é {len(valores[1])} 3 é {len(valores[3])}.')

