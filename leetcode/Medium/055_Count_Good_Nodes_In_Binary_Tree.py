from BTree_Lib import BinaryTree as BT
def count_good_nodes_in_binarytree(tree: BT) -> int:
    def helper(tree: BT | None, max_elem_stack: list[int]) -> int:
        if tree is None or tree.val is None:
            return 0
        this_valid = 0 # if this one is a valid 'good' node
        if max_elem_stack == []: # if it is the first node
            this_valid = 1
            max_elem_stack = [tree.val]
        else:
            if tree.val >= max_elem_stack[-1]:
                # this condition means the current value is equal to, or bigger than max, hence
                this_valid = 1 # this node is valid
                max_elem_stack.append(tree.val)
            else:
                max_elem_stack.append(max_elem_stack[-1])

        lans = helper(tree.left, max_elem_stack)
        rans = helper(tree.right, max_elem_stack)
        max_elem_stack.pop() # since lans and rans have been evaluated, we would pop our current root from stack
        return lans + this_valid + rans
    return helper(tree, [])

# tree = BT.create([5, 3, 2, 6, 4, 7, 1, 3])
# tree.print()
# print(count_good_nodes_in_binarytree(tree))
