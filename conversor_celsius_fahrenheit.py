"Função que converte graus Celsius em graus Fahrenheit"

def conversor():
    celsius = float(input("Digite o valor da temperatura em graus Celsius - Cº:"))
    fahrenheit = celsius * 1.8 + 32
    return f'A temperatura em graus Fahrenheit é de {fahrenheit}ºF'

if __name__ == '__main__':
    print(conversor())