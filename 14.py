def notation(b: int, radix: int) -> list:
    a = []
    while b > 0:
        a.append(b % radix)
        b //= radix
    a.reverse()
    return a


print(sum(notation(6**203+5*6**405-3*6**144+76, 6)))