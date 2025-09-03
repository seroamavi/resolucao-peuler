import math



for x in range(1000):
    for i in range(1000):
        if x + i + math.sqrt(x**2 + i**2) == 1000 and x != 0 and i != 0:
            print(x * i * math.sqrt(x**2 + i**2))
            break

