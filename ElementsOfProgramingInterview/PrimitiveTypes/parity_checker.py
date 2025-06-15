# In this question we present two different parity (number of 1s) checker.
#
# The First one checks the parity manually, that is it goes through each bit
# right to left, and checks whether they are 1 or not (by having n & 1). It they are
# then parity of 1 becomes 0 and parity of 0 becomes 1, and if they are not, parity
# remains same.
def parity_checker_prim(n):
    parity = 0
    while n:
        parity ^= n & 1
        n >>= 1
    return parity

# This one goes through bit repsentation of n, and always cuts it from it's
# least representative occurent of 1 in binary representation. The fact that this
# cutting is even allowed (that our while n loop is still valid) means there is
# at least one more 1 available, hence xoring the parity (to switch 1 -> 0, 0 -> 1)
def parity_checker_adv(n):
    parity = 0
    while n:
        parity ^= 1
        n &= (n - 1)
    return parity
