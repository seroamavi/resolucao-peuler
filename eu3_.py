#Maior fator primo de 600851475143


fprimos = []
is_prime = False
for x in range(2, 31):
    for i in range(1, x + 1):
        if x % i == 0 and i != 1 and i != x:
            is_prime = False
            break

        else:
            is_prime = True

    if is_prime == True:
        fprimos.append(x)

print(fprimos)

