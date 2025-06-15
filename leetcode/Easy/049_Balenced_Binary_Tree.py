from BTree_Lib import BinaryTree
# This algorithm works by using a helper function, which calculates
# whether a particular subnode is valid or not, and what is the height of
# that node. At the rood node we would simply discard the height and return the bool
def is_balenced(tree: BinaryTree) -> bool:
    def helper(tree: BinaryTree | None) -> tuple[bool, int]:
        if tree is None or tree.val is None: # that is this node is invalid, or is once case below
                                             # base case
            return (True, 0)
        leftB, leftH   = helper(tree.left)
        rightB, rightH = helper(tree.right)
        is_balenced = False
        if leftB and rightB and abs(leftH - rightH) <= 1: # if both left node and right node is valid
            is_balenced = True                            # and the diff between height of left and right is smaller than 2
        return (is_balenced, 1 + max(leftH, rightH)) # returning max since we want most height
    ans, _ = helper(tree)
    return ans

# tree = BinaryTree.create([1, 2, 3, 4, 5, 6, 7, 8])
# print(is_balenced(tree))
