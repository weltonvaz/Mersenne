def divisao_comparacao_nao_restauradora(dividendo, divisor):
    """
    Realiza a divisão de inteiros utilizando o algoritmo de comparação não restauradora.

    Args:
        dividendo: O número a ser dividido.
        divisor: O número pelo qual o dividendo será dividido.

    Returns:
        Uma tupla contendo o quociente e o resto da divisão.
    """

    if divisor == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")

    # Garante que dividendo e divisor sejam positivos
    sinal = 1
    if dividendo < 0:
        sinal *= -1
        dividendo = -dividendo
    if divisor < 0:
        sinal *= -1
        divisor = -divisor

    quociente = 0
    resto = dividendo

    for i in range(32, -1, -1):  # Considera 32 bits para inteiros
        resto <<= 1  # Deslocamento à esquerda
        quociente <<= 1  # Deslocamento à esquerda
        if resto >= divisor:
            resto -= divisor
            quociente += 1
        elif resto < 0:
            resto += divisor

    return quociente * sinal, resto * sinal

# Exemplo de uso
dividendo = 29
divisor = 5

quociente, resto = divisao_comparacao_nao_restauradora(dividendo, divisor)

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")