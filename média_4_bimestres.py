"Função que te dá a média de 4 notas bimestrais"

def media_4_notas():
    pri_bi = int(input("Digite a nota do primeiro bimestre: "))
    seg_bi = int(input("Digite a nota do segundo bimestre: "))
    ter_bi = int(input("Digite a nota do terceiro bimestre: "))
    qua_bi = int(input("Digite a nota do quarto bimestre: "))
    media_4_bi = (pri_bi + seg_bi + ter_bi + qua_bi)/4
    return f'A média dos quatro bimestres é {media_4_bi}'

if __name__ == '__main__':
    print(media_4_notas())
