def divisao_newton_raphson(dividendo, divisor, precisao=1e-8):
    """
    Realiza a divisão de inteiros utilizando o método de Newton-Raphson.

    Args:
        dividendo: O número a ser dividido.
        divisor: O número pelo qual o dividendo será dividido.
        precisao: A precisão desejada para o cálculo do inverso.

    Returns:
        Uma tupla contendo o quociente e o resto da divisão.
    """

    if divisor == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")

    # Encontra o inverso aproximado do divisor usando Newton-Raphson
    x = 1.0 / divisor  # Estimativa inicial
    while abs(divisor * x - 1) > precisao:
        x = x * (2 - divisor * x)  # Iteração de Newton-Raphson

    # Calcula o quociente e o resto
    quociente = int(dividendo * x)
    resto = dividendo - quociente * divisor

    return quociente, resto

# Exemplo de uso
dividendo = 29
divisor = 5

quociente, resto = divisao_newton_raphson(dividendo, divisor)

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")