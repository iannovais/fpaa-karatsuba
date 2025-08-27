def karatsuba(num1: int, num2: int, n: int) -> int:
    if n <= 3:
        return num1 * num2

    m = (n + 1) // 2
    p, q = quebrar_num(num1, m)
    r, s = quebrar_num(num2, m)

    pr = karatsuba(p, r, m)
    qs = karatsuba(q, s, m)
    y = karatsuba(p + q, r + s, m + 1)

    uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs
    return uv

def quebrar_num(num: int, m: int) -> tuple[int, int]:
    return divmod(num, 10 ** m)
