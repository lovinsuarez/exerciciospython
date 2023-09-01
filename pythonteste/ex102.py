def fatorial(n, Show=False):
    """
    -> calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param Show:(opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if Show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, Show=True))