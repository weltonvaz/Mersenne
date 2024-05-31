def divisao_srt_simplificada(dividendo, divisor):
    """
    Simulação simplificada do algoritmo de divisão SRT.

    Args:
        dividendo: O número a ser dividido.
        divisor: O número pelo qual o dividendo será dividido.

    Returns:
        Uma tupla contendo o quociente e o resto da divisão.
    """

    if divisor == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")

    # Tabela de pesquisa simplificada para SRT (apenas alguns valores)
    tabela_srt = {
        1: 1,
        2: 5,
        3: 3,
        4: 2,
        5: 5,
    }

    quociente = 0
    resto = dividendo

    while resto >= divisor:
        # Encontra o maior múltiplo do divisor que é menor ou igual ao resto
        multiplicador = max(k for k in tabela_srt if k * divisor <= resto)

        # Estima o quociente usando a tabela SRT
        quociente_estimado = tabela_srt[multiplicador]

        # Atualiza o resto e o quociente
        resto -= multiplicador * divisor
        quociente += quociente_estimado

    return quociente, resto

# Exemplo de uso
dividendo = 29
divisor = 5

quociente, resto = divisao_srt_simplificada(dividendo, divisor)

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente (aproximado): {quociente}")
print(f"Resto: {resto}")