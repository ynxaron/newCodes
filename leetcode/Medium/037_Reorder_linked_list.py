from Node_Lib import Node # using a liberary where our node is defined
# The crux of this algorithm depends upon first converting a linked list
# to a list, then using a two pointer technique, l at 0 and r = len(node.to_list()) - 1,
# and doing after appending the values (l += 1) and (r -= 1)
def reorder_linked_list(node: Node) -> Node:
    stack = node.to_list()
    rl = 0
    sl = len(stack) - 1
    root = Node()
    nroot = root # using a nroot, 'new' root, which would remain pointed at first element

    while rl < sl:
        root.val = stack[rl]
        root.next = Node()
        root = root.next
        root.val = stack[sl]
        root.next = Node()
        root = root.next
        rl += 1
        sl -= 1

    if rl == sl: # if rl == sl, that is an element that is in between has remained unpushed, and pushing it
        root.val = stack[rl]
    else: # we are using this to clean all the Nones that are for strange reason still present
        nroot.remove_nones()
    return nroot

n = Node.create([1, 2, 3, 4, 5, 6])
print(n.len())
m = reorder_linked_list(n)
