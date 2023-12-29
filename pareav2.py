import decimal

# define a precisão decimal
decimal.getcontext().prec = 100

# área do retângulo
n = 1283
area = ((2**n)-1)
count = 0
# encontrar a base e a altura
for i in range(1, int(decimal.Decimal(area).sqrt()) + 1):
    if area % i == 0:
        base = i
        altura = area // i
        count += 1

# cálculo do perímetro
perimetro = 2 * (base + altura)

print("area: ", area) 
print("Base:", base)
print("Altura:", altura)
print("Perímetro:", perimetro)
print("contador: ", count)
