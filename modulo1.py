p = 31 # seu número primo aqui
M_p = 2**p - 1
s = 4
count = 0
for n in range(p - 2):
    s = (s**2 - 2) % M_p
    count += 1
print("---- CALCULOS CONCLUÍDOS ----")
print(s)
print(count, "interações")
