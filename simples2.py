n = 129737749
np = ((2**n)-1)*(2**(n-1))
count = 1
while True:
    np = np//2
    udigito = np%10
    if udigito % 2 == 0:
        count += 1
    else:
        count += 1
        print(count)
        break
        

