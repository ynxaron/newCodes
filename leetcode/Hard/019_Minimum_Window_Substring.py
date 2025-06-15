def minimum_window_substring(inp: str, k: str) -> str:
    if inp == "": return ""
    key_map = {}
    for c in k:
        key_map[c] = 1 + key_map.get(c, 0)
    window_map = {}
    have, need = 0, len(key_map)
    min_len, min_str = float("inf"), [-1, -1]
    l = 0
    for r in range(len(inp)):
        window_map[inp[r]] = 1 + window_map.get(inp[r], 0)
        if inp[r] in key_map and window_map[inp[r]] == key_map[inp[r]]:
            have += 1

        while have == need:
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                min_str = [l, r]
            window_map[inp[l]] -= 1
            if inp[l] in key_map and window_map[inp[l]] < key_map[inp[l]]:
                have -= 1
            l += 1

    minL, minR = min_str
    return inp[minL:minR + 1] if min_len != float("inf") else ""

print(minimum_window_substring("HCMALCITAM", "CAT"))
