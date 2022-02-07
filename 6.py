def nine(b: int) -> list:
    a = []
    while b > 0:
        a.append(b % 9)
        b //= 9
    a.reverse()
    return a


print(nine(81**5+3**30-27).count(8))