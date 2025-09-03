n = 20
divisible = False
numeros = [i for i in range(1,21)]
while not divisible:
    n += 1
    b = list(filter(lambda x: n % x == 0, numeros))
    if len(b) == 20:
        divisible = True


print(n)


