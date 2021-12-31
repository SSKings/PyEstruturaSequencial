"Função que calcula a área de um quadrado e mostra o dobro do valor"

def area2_quadrado():
    print("Calculando a área do quadrado e mostrando o dobro do valor")
    base = float(input("Digite o valor da base do quadrado: "))
    altura = float(input("Digite o valor da altura do quadrado: "))
    area = base * altura
    return f'O dobro da área é {area*2}'

if __name__ == '__main__':
    print(area2_quadrado())