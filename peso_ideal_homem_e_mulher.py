"função que calcula o peso ideal a partir da altura para homens e mulheres"

def peso_ideal():
    altura = float(input("Digite a sua altura em metros: "))
    p_ideal_h = (72.7 * altura) - 58
    p_ideal_m = (62.1 * altura) - 44.7
    return f'''O peso ideal para um homem dessa altura é de {p_ideal_h}kg.
Para uma mulher o peso ideal é de {p_ideal_m}kg.
'''

if __name__ == '__main__':
    print(peso_ideal())