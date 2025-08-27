def karatsuba(num1: int, num2: int, n: int = None) -> int: #n1
    if n is None: #n2
        n = max(len(str(num1)), len(str(num2))) #n3

    if n <= 3: #n4 
        return num1 * num2 #n5

    m = (n + 1) // 2 #n6
    p, q = quebrar_num(num1, m) #n7
    r, s = quebrar_num(num2, m) #n8

    pr = karatsuba(p, r, m) #n9
    qs = karatsuba(q, s, m) #n10
    y  = karatsuba(p + q, r + s, m + 1) #n11

    return pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs #n12

def quebrar_num(num: int, m: int) -> tuple[int, int]:
    return divmod(num, 10 ** m)