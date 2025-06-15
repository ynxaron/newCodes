from BTree_Lib import BinaryTree as BT
# The crux of this algorithm is to use a custom function defined internally which
# would do a recursive search, with two base cases. One in which the node is None
# and other in which the value of that node matches our given value
def lowest_common_denominater(tree: BT, p: int, q: int) -> BT:
    psearch_stack = []
    qsearch_stack = []

    def search(tree: BT | None, item: int, search_stack: list[BT]) -> None | list[BT]:
        # in first base case, this signifies this particular path was fruitless, rollback
        if tree is None or tree.val is None:
            return None
        # in second base case, this signifies this particular path was fruitfull, use this
        if tree.val == item:
            return search_stack

        # if Two base cases does not apply, then append this value at our stack
        # meaning we are considering this stack value as one in the path
        search_stack.append(tree)
        lans = search(tree.left, item, search_stack)
        # if a path exists in our left value, then just return this path, which would be carried to the top
        if lans is not None:
            return lans

        # If left search fails do the right search, then just return this path if it exists
        rans = search(tree.right, item, search_stack)
        if rans is not None:
            return rans

        # if neither it's left child nor right child has the path, then remove this node value from our stack
        search_stack.pop()
        return None

    search(tree, p, psearch_stack) # doing this to two different stacks
    search(tree, q, qsearch_stack)

    last = tree
    i = 0
    # then finding the last value at which both 'p' and 'q' have been found from the node,
    # this would guarentee to have the main root value as default, so it won't fail
    while i < min(len(psearch_stack), len(qsearch_stack)) and psearch_stack[i] == qsearch_stack[i]:
        last = psearch_stack[i]
        i += 1

    return last
