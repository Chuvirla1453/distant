def notation(b: int, radix: int) -> list:
    a = []
    while b > 0:
        a.append(b % radix)
        b //= radix
    a.reverse()
    return a


print(len(set(notation(2**51+2**40+2**35+2**17-2**5, 16))))