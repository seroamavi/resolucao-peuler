def isEven(x):
    if x % 2 == 0:
        return True
    
    else:
        return False



if __name__ == "__main__":
    a, b = 1, 0
    c = 0 
    l = []
    while a < 4000000:
        l.append(a)
        a, b = a + b, a

    s = sum(filter(isEven, l))
    print(s)    