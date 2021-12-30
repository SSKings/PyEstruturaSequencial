"Função que cumprimenta com um Hello"

def hello():
    name = input("Qual o Seu nome? ")
    return f'Hello! {name}'

if __name__ == '__main__':
    print(hello())
