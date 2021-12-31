"Função que pede valor da hora de trabalho e horas trabalhadas e retorna o valor do salário"

def valor_salario():
    v_hora = float(input("Quanto você ganha por hora?"))
    h_trabalho = float(input("quantas horas trabalhou no mês?"))
    salario = v_hora * h_trabalho
    return f'O seu salário é de:--R${salario}--'

if __name__ == '__main__':
    print(valor_salario())
