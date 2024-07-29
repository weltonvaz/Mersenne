# Definindo os valores de p e a
p = 2047
a = 89

# Calculando a^(p-1) % p
resultado = pow(a, p-1, p)

# Exibindo o resultado
print(f'O resultado de {a}^{p-1} % {p} é: {resultado}')

# Verificando se o resultado é igual a 1
if resultado == 1:
    print(f'{p} pode ser primo segundo o teste de Fermat com a base {a}.')
else:
    print(f'{p} não é primo segundo o teste de Fermat com a base {a}.')
