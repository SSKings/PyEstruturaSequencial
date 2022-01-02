"Função que soma dois números"

def soma_2():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    soma = n1 + n2
    return f'A soma dos dois é: {soma}'


print(soma_2())
