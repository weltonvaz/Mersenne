import decimal

# Define a precisão
decimal.getcontext().prec = 1000

def retangulo_otimizado(area):
    # Converte a área para um número decimal
    area = decimal.Decimal(area)

    # Inicializa a largura como a raiz quadrada da área
    largura = area.sqrt().to_integral_value(rounding=decimal.ROUND_DOWN)

    # Encontra o par de inteiros cujo produto é a área e cuja diferença é a menor possível
    while area % largura != 0:
        largura -= 1

    comprimento = area // largura

    return largura, comprimento

# Testa a função
area = (2**1259)-1
largura, comprimento = retangulo_otimizado(area)
print(f"Para uma área de {area}, as dimensões otimizadas do retângulo são {largura} x {comprimento}.")
