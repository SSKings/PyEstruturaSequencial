"Função que solicita e mostra um número"

def mostrar_num():
    numero = int(input("Digite um número: "))
    return f'O número informado foi {numero}'

if __name__ == '__main__':
    print(mostrar_num())