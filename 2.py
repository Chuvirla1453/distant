def min_radix(b: int, c: int) -> None:
    bb = b
    for i in range(2, 38):
        b = bb
        a = []
        while b > 0:
            a.append(b % i)
            b //= i
        if len(a) == c:
            print(i)
            return


min_radix(50, 2)
