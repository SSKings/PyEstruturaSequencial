"Função que converte graus Fahrenheit em graus Celsius"

def conversor():
    fahrenheit = float(input("Digite o valor da temperatura em graus Fahrenheit - Fº:"))
    celsius = 5 * ((fahrenheit-32) / 9)
    return f'A temperatura em graus Celsius é de {celsius}ºC'

if __name__ == '__main__':
    print(conversor())