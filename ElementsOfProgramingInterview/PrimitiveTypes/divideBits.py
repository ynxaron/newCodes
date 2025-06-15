def divide(n, m):
    n, m = max(n, m), min(n, m)
    def sub(n, m):
        carry = 0
        res = 0
        i = 0
        while n:
            tempres = (n & 1) ^ (m & 1) ^ carry
            if carry == 0:
                if (n & 1) == 0 and (m & 1) == 0:
                    carry = 1
            if carry == 1:
                if (n & 1) == 1 and (m & 1) == 0:
                    carry = 0

            res |= (tempres << i)
            n >>= 1
            m >>= 1
            i += 1

    res = 0
    while n >= m:
        n = sub(n, m)
        res += 1

    return res
