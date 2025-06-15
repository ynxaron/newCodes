# The idea is to xor each element of the binary representation with each other
# so we begin by swapping 32-left most bits with 32-right most bits, and since we
# only want ourselves to be concerned with left-most 32 bit value, we and this
# (000..32 times)..(111..32 times), leading to all 32 right most value being 0
# and 32 left most values remaining the same. And we descrease this 32 by half each time
def parity(x):
    x ^= (x >> 32) & bin(2 ** 32 - 1)
    x ^= (x >> 16) & bin(2 ** 16 - 1)
    x ^= (x >> 8) & bin(2 ** 8 - 1)
    x ^= (x >> 4) & bin(2 ** 4 - 1)
    x ^= (x >> 2) & bin(2 ** 2 - 1)
    x ^= (x >> 1) & bin(2 ** 1 - 1)
    return x & 0x1
