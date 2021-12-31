"Função que pede o raio para calcular a área do círculo"

def area_do_circulo():
    print("Calculando a área de um círculo")
    raio = float(input("Digite o valor do raio: "))
    pi = 3.14159265359
    area = pi * raio**2
    return f'O valor da área do círculo é: {area}'

if __name__ == '__main__':
    print(area_do_circulo())
