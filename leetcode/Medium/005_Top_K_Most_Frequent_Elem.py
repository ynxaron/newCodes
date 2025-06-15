# Using a bucket such that the count becomes it's index, after which
# iterating it in reverse order and appending the elements found into
# our result array, checking after each append if we have reached our limit (k)
def top_k_elem(inp: list[int], k: int) -> list[int]:
    count_map = {}
    # Creating a count map
    for e in inp:
        count_map[e] = 1 + count_map.get(e, 0)

    # Using len(inp) so that, at max, there is a single element occuring all the times
    # and it would have an index equal to len(inp)
    bucket = [[] for _ in range(len(inp))]
    for item, count in count_map.items():
        bucket[count].append(item) # appending in case there are more than one element with a same count

    i = 0
    res = []
    for item_list in reversed(bucket):
        # iterating over the item found at a specific count, appending each to our array
        # Beginning from the end since that would have the biggest index, hence most count
        for item in item_list:
            res.append(item)
            i += 1
            if i == k: # checking if we have reached our threshold
                return res
    return res

print(top_k_elem([1, 1, 1, 2, 2, 3], 2))
