import numpy as np

def int_to_list(n):
    """Converte um número inteiro em uma lista de dígitos binários."""
    return [int(digit) for digit in bin(n)[2:]]

def list_to_int(lst):
    """Converte uma lista de dígitos binários em um número inteiro."""
    return int(''.join(map(str, lst)), 2)

def multiply_fft_integer(a, b):
    """Multiplica dois números inteiros grandes usando a FFT e retorna o produto como um inteiro."""

    # Converte os números inteiros em listas de dígitos binários
    a = int_to_list(a)
    b = int_to_list(b)

    n = len(a)
    m = len(b)

    # Calcula o tamanho adequado para a transformada rápida de Fourier
    size = 2**(int(np.log2(n + m - 1)) + 1)

    # Calcula as transformadas rápidas de Fourier dos polinômios
    fft_a = np.fft.fft(a, size)
    fft_b = np.fft.fft(b, size)

    # Multiplica os resultados das transformadas no domínio da frequência
    fft_result = fft_a * fft_b

    # Calcula a transformada inversa para obter o resultado no domínio do tempo
    result = np.fft.ifft(fft_result).real.round().astype(int)

    # Remove zeros à esquerda
    while len(result) > 1 and result[-1] == 0:
        result = result[:-1]

    # Retorna o resultado como um número inteiro
    return list_to_int(result[::-1])

def lucas_lehmer(p):
    """Executa o teste de Lucas-Lehmer para um número primo de Mersenne com expoente p."""

    # Inicializa s com 4
    s = 4

    # Calcula M_p, o número primo de Mersenne com expoente p
    M_p = 2**p - 1

    # Executa o teste de Lucas-Lehmer
    for _ in range(p - 2):
        # Usa a função multiply_fft_integer para multiplicar s por si mesmo
        s_squared = multiply_fft_integer(s, s)

        # Calcula o próximo valor de s
        s = (s_squared - 2) % M_p

    # Retorna True se s é 0 (indicando que M_p é primo), False caso contrário
    return s == 0

def main():
    # Solicita ao usuário um número inteiro
    p = int(input("Digite um número inteiro: "))

    # Executa o teste de Lucas-Lehmer
    if lucas_lehmer(p):
        print("Primo")
    else:
        print("Não primo")

if __name__ == "__main__":
    main()
