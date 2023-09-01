tot18 = 0
totH = 0
totm20 = 0
print('Cadastre uma pessoa')
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]? ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'total de pessoas com mais de 20 anos: {totm20}')
print(f'ao todo temos {totH} homens cadastrados')
print(f'total de pessoas com mais de 18 anos {tot18}')
