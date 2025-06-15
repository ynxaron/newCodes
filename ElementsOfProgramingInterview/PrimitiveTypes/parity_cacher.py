# Containing cached parities of predefined values
# We would be dividing our number into four parts of two bites each, then caching
# all partieis of all possible two-byte value in a dictonary, then simply right shifting
# to get whether the last two bytes, the second last two bytes, etc. We are also & by 3
# defined as 0b11, to negate all other values that came before it
PREDEFINED_PARITY = {'0b00': 0, '0b01': 1, '0b10': 1, '0b11': 0}
def calculate_parity(n):
    parity = PREDEFINED_PARITY[bin(n >> 6)] ^ PREDEFINED_PARITY[bin((n >> 4) & 3)] ^ PREDEFINED_PARITY[bin((n >> 2) & 3)] ^ PREDEFINED_PARITY[bin(n & 3)]
    return parity

print(calculate_parity(25))
