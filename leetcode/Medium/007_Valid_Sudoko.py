# The method is to use threee hasmaps, one for the rows, one for columns, and one for the
# sqr it was in. Whenever it encountered a new element, it checks if it is in rows[r], cols[c]
# or, this is the interesting part, sqrs[(r // 3, c // 3)], dividing to see on which sqr the element
# in consideration truly is in
def valid_sudoko(inp: list[list[str]]) -> bool:
    rows = {}
    cols = {}
    sqrs = {}

    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if inp[r][c] == ".": # Indicating that the element is empty (as specified by the problem)
                continue

            if (inp[r][c] in rows[r]) or (inp[r][c] in cols[c]) or (inp[r][c] in sqrs[(r // 3, c // 3)]):
                # Here, any number from 0->2 would become 0, 3->5 would become 1 and 6->9 would become 2
                # indicating which sqr it was in
                return False

            # Appending if there were none
            rows[r].append(inp[r][c])
            cols[c].append(inp[r][c])
            sqrs[(r // 3, c // 3)].append(inp[r][c])
    return True
