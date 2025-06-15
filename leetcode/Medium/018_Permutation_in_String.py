def permutation_in_string(inp: str, k: str) -> bool:
    def inx(c: str) -> int:
        if ord(c) > 90:
            return ord(c) - ord('a')
        else:
            return ord(c) - ord('A')

    k_array = [0] * 26
    for c in k:
        k_array[inx(c)] += 1

    inp_array = [0] * 26
    for c in inp[:len(k)]:
        inp_array[inx(c)] += 1

    matches = 0
    for i in range(26):
        matches += 1 if k_array[i] == inp_array[i] else 0

    for i in range(len(k), len(inp)):
        if matches == 26:
            return True

        if inp[i] in k:
            matches += 1
        else:
            matches -= 1

        if inp[i - len(k)] in k:
            matches -= 1
        else:
            matches += 1
    return False

print(permutation_in_string("eidbaooo", "ab"))
