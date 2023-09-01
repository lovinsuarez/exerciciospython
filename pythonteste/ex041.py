from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('CLASSSIFICAÇÃO MIRIM.')
elif idade <= 14:
    print('CLASSIFICAÇÃO INFANTIL.')
elif idade <= 19:
    print('CLASSIFICAÇÃO JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO SÊNIOR.')
else:
    print('CLASSIFICAÇÃO MASTER.')
