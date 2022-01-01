"função que calcula o peso ideal a partir da altura"

def peso_ideal():
    altura = float(input("Digite a sua altura em metros: "))
    p_ideal = (72.7 * altura) - 58
    return f' O seu peso ideal é de {p_ideal}kg'

if __name__ == '__main__':
    print(peso_ideal())