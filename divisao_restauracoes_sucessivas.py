def divisao_restauracoes_sucessivas(dividendo, divisor):
  """
  Realiza a divisão de inteiros utilizando o algoritmo de restaurações sucessivas.

  Args:
    dividendo: O número a ser dividido.
    divisor: O número pelo qual o dividendo será dividido.

  Returns:
    Uma tupla contendo o quociente e o resto da divisão.
  """

  if divisor == 0:
    raise ZeroDivisionError("Divisão por zero não é permitida.")

  quociente = 0
  resto = dividendo

  while resto >= divisor:
    resto -= divisor
    quociente += 1

  return quociente, resto

# Exemplo de uso
dividendo = 29
divisor = 5

quociente, resto = divisao_restauracoes_sucessivas(dividendo, divisor)

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")