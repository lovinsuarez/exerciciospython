nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome em maiusculas é {} '.format(nome.upper()))
print('Analisando seu nome em minusculo é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))