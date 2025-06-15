def valid_parentheses(inp: str) -> bool:
    sqr, circle, cur = 0, 0, 0
    for c in inp:
        if c == "[":
            sqr += 1
        if c == "]":
            sqr -= 1
        if c == "(":
            circle += 1
        if c == ")":
            circle -= 1
        if c == "{":
            cur += 1
        if c == "}":
            cur -= 1

        if (sqr < 0 or circle < 0 or cur < 0): # since ()) or {}} does not make sense
            return False
    return (sqr == 0 and circle == 0 and cur == 0) # and all brackets that are opened must be closed
