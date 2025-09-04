c = 0
n = 2
while c != 10001:
    for x in range(1, n + 1):
        if n % x == 0 and (x != 1 and  x != n):
            break

    else:
        c += 1

    if c == 10001:
        break

    n += 1
    


print(n)

