n = 43
np = ((2**n)-1)*(2**(n-1))
count = 0
while True:
    a = divmod(np,2)
    if a[1] == 0:
        np = a[0]
        count += 1
    else:
        break
print(count)
print(np)