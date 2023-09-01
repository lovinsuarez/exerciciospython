n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opção = int(input('O que voce quer fazer com os valores? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} e {} da {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {} e {} é {}.'.format(n1,n2, mult))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        else:
            print('{} é maior'.format(n2))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('digite o segundo valor: '))
    elif opção == 5:
        print('Opção inválida tente novamente!')
print('Fim do programa, volte sempre')