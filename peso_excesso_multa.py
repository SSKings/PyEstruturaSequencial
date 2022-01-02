"Função que pede o peso, ver se peixes estão dentro do regulamento e se há multa"

def regulamento():
    peso = float(input("Digite o peso da quantidade de peixes:"))
    excesso = peso - 50
    multa = excesso * 4
    if peso > 50:
        return f'''O peso excedeu {excesso}kg a mais do que o permitido e a multa a ser paga é de R${multa}'''
    else:
        return f'O peso não excede o limite e não há multa a ser paga.'
if __name__ == '__main__':
    print(regulamento())