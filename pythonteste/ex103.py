def ficha(jog='<desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gol(s) no campeonato.')


#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
