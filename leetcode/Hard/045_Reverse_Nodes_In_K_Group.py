from Node_Lib import Node
# The crux of the algorithm relies on reversing small batches of the node,
# keeping track of two additional pointers, one that would tell from where to
# begin the reversing, and where to end it. One we would call 'm', from where
# to begin the reversing, and another 'b', that would join the previously reversed
# batch with the newly reversed batch
def reverse_nodes_in_k_group(n: Node, k: int) -> Node:
    m, b = n, None # keeping track of where to begin the reversing, and how to knit reverse batches
    root = None
    nlen = n.len()
    lendivkmulk = (nlen // k) * k
    # since we are going to knit only batches of 'k', if there are
    # certain remainders that is smaller than 'k', we don't want to consider them
    inx = 1
    while inx <= lendivkmulk:
        if inx % k == 0: # now we can make this 'n' the end of a batch
            prev, curr = None, m
            while curr is not None and curr != n: # reversing just before we hit 'n'
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            if curr is not None: # making the last element point backwards
                nxt = curr.next
                curr.next = prev
                if root is None: # making the first 'n' the root, from where it would begin
                    root = curr
                if b is not None: # if previous batches had been reversed, knit it back
                    b.next = curr
                # updating b, n, m
                b = m
                n = nxt
                m = n
        else:
            n = n.next
        inx += 1
    if lendivkmulk < nlen: # stiching the remaining elements that don't add up to 'k', hence can't be reversed
        b.next = n
    return root

# n = Node.create([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# n.print()
# reverse_nodes_in_k_group(n, 3).print()
