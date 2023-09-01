n = int(input('Digite um númro para calcular o fatorial: '))
c = n
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
#('O fatorial de {} é {}'.format(n, f))
