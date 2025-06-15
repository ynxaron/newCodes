# The objective is to use use the two sum solution, but make target the -inp[i]
def three_sum(inp: list[int]) -> list[list[int]]:
    ans = []
    ans_seen = {} # to make sure we are not pushing duplicates, that are present
    for i in range(len(inp)):
        seen = {}
        target = -inp[i] # hence if succeding, inp[j] and (target - inp[j]) would equal -inp[i]
        for j in range(len(inp)):
            if j == i: # skipping since we can't take same element twice
                continue
            if (target - inp[j]) in seen: # if we found a match
                this_list = [inp[i], inp[j], target - inp[j]]
                this_list.sort() # sorting since a permutation of a list is still the same list
                if tuple(this_list) not in ans_seen:
                    ans_seen[tuple(this_list)] = True
                    ans.append(this_list)
            seen[inp[j]] = True
    return ans

print(three_sum([-1, 0, 1, 2, -1, -4]))
