"Função que recebe valor da hora e horas trabalhadas e retorna o valor de um salário descontado os devidos impostos"


def salario_real():
    v_hora = float(input("Digite o valor da hora de trabalho: "))
    q_horas = float(input("Digite a quatidade de horas de trabalho "))
    salario_bruto = v_hora * q_horas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    desconto_total = ir + inss + sindicato
    salario_liquido = salario_bruto - desconto_total
    return f'''- O Salário Bruto : R${salario_bruto}
- IR (11%) : R${ir}
- INSS (8%) : R${inss}
- Sindicato ( 5%) : R${sindicato}
= Salário Liquido : R${salario_liquido}
'''

if __name__ == '__main__':
    print(salario_real())
