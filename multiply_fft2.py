import numpy as np

def int_to_list(n):
    """Converte um número inteiro em uma lista de dígitos."""
    return [int(digit) for digit in str(n)]

def list_to_int(lst):
    """Converte uma lista de dígitos em um número inteiro."""
    return int(''.join(map(str, lst)))

def multiply_fft_integer(a, b):
    """Multiplica dois números inteiros grandes usando a FFT e retorna o produto como um inteiro."""

    # Converte os números inteiros em listas de dígitos
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

def main():
    # Exemplos de números a serem multiplicados.
    a = 89
    b = 23

    # Multiplica os números usando a FFT.
    product = multiply_fft_integer(a, b)

    # Imprime o produto.
    print(product)

if __name__ == "__main__":
    main()
