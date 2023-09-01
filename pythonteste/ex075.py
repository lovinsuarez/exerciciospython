num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'você digitou os valores {num}')
print(f'O valor 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'o valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')