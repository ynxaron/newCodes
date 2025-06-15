from BTree_Lib import BinaryTree
def maximum_depth(tree: BinaryTree) -> int:
    leftDepth, rightDepth = 0, 0
    if tree.left is not None and tree.left.val is not None:
        # that is that there is a left tree to consider
        leftDepth = maximum_depth(tree.left)
    if tree.right is not None and tree.right.val is not None:
        # that is that there is a right tree to consider
        rightDepth = maximum_depth(tree.right)
    return 1 + max(leftDepth, rightDepth)

tree = BinaryTree.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
tree.print()
print(maximum_depth(tree))
