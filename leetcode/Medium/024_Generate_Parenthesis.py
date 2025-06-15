# The crux of this algorithm is to use a recursive function
# that sums the alternatives available
def generate_parenthesis(k: int) -> list[str]:
    res = []
    paren_stack = []

    def ps_generater(l, r):
        if l == r == k: # if all open and close parenthesis are equal to k, append it as an answer
            res.append("".join(paren_stack))

        if l < k: # open parenthesis
            paren_stack.append('(')
            ps_generater(l + 1, r) # call the funcion after a left parenthesis have been added
            paren_stack.pop()      # pop it after all valid alternatives from left pushing has been done

        if r < l: # close parenthesis
            paren_stack.append(')') # call the function after a right parenthesis have been added
            ps_generater(l, r + 1)  # pop it after all valid alternatives from right pushing has been added
            paren_stack.pop()

    ps_generater(0, 0) # begin this function at (0, 0)
    return res

print(generate_parenthesis(5))
