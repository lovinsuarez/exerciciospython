termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

t = int(input('Quantos termos deseja mostrar:'))
a = 1
controle = 1
while t != 0:
    if controle <= t:
        print('{}º termo: {}'.format(a, termo1 + razao * (a - 1)))
        a += 1
        controle += 1
    else:
        t = int(input('Deseja visualizar mais quantos termos? '))
        controle = 1