# área do retângulo
n = 116738927
area = ((2**n)-1)

# encontrar a base e a altura
for i in range(1, int(area ** 0.5) + 1):
    if area % i == 0:
        base = i
        altura = area // i

# cálculo do perímetro
perimetro = 2 * (base + altura)

print("Base:", base)
print("Altura:", altura)
print("Perímetro:", perimetro)