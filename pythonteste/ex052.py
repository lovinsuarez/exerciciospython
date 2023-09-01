num = int(input('Digite um número: '))
tot = 0
for a in range (1, num + 1):
    if num % a == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(a), end='')
print('\n\033[mO numero foi divisivel {} vezes'.format(num, tot))