# The crux of this algorithm is to notice that whenever we encounters
# an element smaller than before, we make our buy option there, and then
# simply calculate the profit every other time, making it a max if the difference
# is larger than seen before
def best_time_to_buy_sell(inp: list[int]) -> int:
    max_profit = 0
    l = 0 # the smallest seen element so far is the one at the beginning
    for r in range(len(inp)):
        if inp[l] < inp[r]: # if this element is larger than our smallest one, then take the profit and compare
            max_profit = max(max_profit, inp[r] - inp[l])
        else:
            l = r # else change our buy option here, since any profit we would be able to make by having previous opotion
            # we would be able to increase by taking this new element as the buy option
    return max_profit

print(best_time_to_buy_sell([7, 1, 5, 3, 6, 4]))
