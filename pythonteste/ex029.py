velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
