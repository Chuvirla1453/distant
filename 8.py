def notation(b: int, radix: int) -> list:
    a = []
    while b > 0:
        a.append(b % radix)
        b //= radix
    a.reverse()
    return a


n = notation(4**3*3**19, 3)
print(f'0: {n.count(0)}')
print(f'1: {n.count(1)}')
print(f'2: {n.count(2)}')