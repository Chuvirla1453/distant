def notation(b: int, radix: int) -> list:
    a = []
    while b > 0:
        a.append(b % radix)
        b //= radix
    a.reverse()
    return a


c = 0
for i in range(2, 11):
    n = notation(3456, i)
    for j in n:
        if j % 2:
            break
    else:
        c += i
print(c)