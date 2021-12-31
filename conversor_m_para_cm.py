"Função que converte metros para centimetros"

def m_para_cm():
    print("Convertendo metros para centimetros\n")
    v_metros = float(input("Digite o valor em metros: "))
    v_centimetros = v_metros * 100
    return f'Esse é o valor em centimetros --> {v_centimetros}cm'

if __name__ == '__main__':
    print(m_para_cm())
