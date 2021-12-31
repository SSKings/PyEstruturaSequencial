"Função que calcula a área de um quadrado e imprime o dobro do valor"

def area2_quadrado():
    print("O dobro da área do quadrado\n\n\n")
    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))
    area = base * altura
    return f'O dobro da área é {area}'

if __name__ == '__main__':
    print(area2_quadrado())