def área(largura, comprimento):
    m4 = largura * comprimento
    print(f'A área de seu terredo de {largura}x{comprimento} é de {m4}m².')


#programa principal
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(largura=l, comprimento=c)
