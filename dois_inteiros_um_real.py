"Programa que pede dois números inteiros e um real e mostra resultados"

def resultados():
    """função que pede os números e gera os resultados
    a)O produto do dobro do primeiro com metade do segundo.
    b)A soma do triplo do primeiro com o terceiro
    c)O terceiro elevado ao cubo.

    :return:
    """
    num_1 = int(input("Digite o primeiro número inteiro:"))
    num_2 = int(input("Digite o segundo número inteiro:"))
    num_3 = float(input("Digite o número real:"))
    a = (num_1*2)*(num_2/2)
    b = (num_1*3) + num_3
    c = num_3**3
    return f'''a)O produto do dobro do primeiro com metade do segundo é:{a}
b)A soma do triplo do primeiro com o terceiro é:{b}
c)O terceiro elevado ao cubo é:{c}'''

if __name__ == '__main__':
    print(resultados())