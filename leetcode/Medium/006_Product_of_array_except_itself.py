# In this example we are using a clever trick where
# the element in res[i] is the product of all elems in input
# before and after it. So, we iterate first from left to right, then right to left
def product_of_array(inp: list[int]) -> list[int]:
    res = [1] * len(inp)
    prefix = 1
    for i in range(len(inp)):
        res[i] = prefix # appending before updating such that it would always be one element behind
        prefix *= inp[i] # which is what we want

    postfix = 1
    for i in range(len(inp) - 1, -1, -1): # doing the same in the reverse order
        res[i] *= postfix # however not merely assinging, since it already holds value before
        postfix *= inp[i]

    return res

print(product_of_array([1, 2, 3, 4]))
print(product_of_array([-1, 1, 0, -3, 3]))
