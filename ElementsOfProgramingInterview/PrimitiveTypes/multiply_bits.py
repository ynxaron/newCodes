# Question: Multiply x and y
#
# We can imagine multiplication as repeated addition, that to multiply x & y
# is to add x to itself a total of y times. We can achieve this by understanding
# the traditional multiplication algorithm. Say we have a function add, add takes
# n and m and returns to us there addition (say we have it, we would worry about
# implementations later). Then after first addition (adding n to 0), we would have n.
# Then, we won't be adding n to itself, rather it would be a right shifted n (just like
# in our textbook algorithms). We would only add n to (right shifted) n whenever the
# ith least significant value of m is 1, otherwise it would be 0.
def mul(n: int, m: int):
    def add(n: int, m: int):
        # For addition we take a xor of lst ith value of m and n, and a carry
        # Then we update a carry whether or not two of these three values are 1 or not.
        # Then we take this tempres, shift it right (by i which we increment each time)
        # and or this would res itself.
        res = 0
        carry = 0
        i = 0
        while n:
            tempres = (m & 1) ^ (n & 1) ^ carry
            carry = (m & n) | (carry & m) | (carry & n)
            res |= (tempres << i)
            m >>= i
            n >>= i
            i += 1
        return res

    res = 0
    while m:
        if m & 1:
            res = add(res, n)
        m = m >> 1
        n = n << 1
    return res
