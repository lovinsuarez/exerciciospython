sexo = str(input('Insira o sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'mMfF':
    sexo = str(input('Dados invalidos, digite novamente [M/F]: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso.'.format(sexo))
