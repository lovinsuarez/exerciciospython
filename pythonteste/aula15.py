n = s = v = 0
while True:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s += n
    v += 1
print(f'A soma vale {s} e voce digitou {v} valores')
