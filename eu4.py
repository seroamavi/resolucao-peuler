palindromes = []
for x in range(100, 1000):
    for i in range(100, 1000):
        if str(x*i) == str(x*i)[::-1]:
            palindromes.append(x*i)


greatest = list(set(palindromes))
greatest.sort()
greatest.reverse()
print(greatest[0])


