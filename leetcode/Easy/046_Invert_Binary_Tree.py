from BTree_Lib import BinaryTree
# We are inverting a binary tree by simply first inverting the left child, the right child,
# then placing the left child at right child's place and right child at left child's place
def invert_tree(tree: BinaryTree | None):
    if tree is None or tree.val is None:
        return

    lft = tree.left
    tree.left = tree.right
    tree.right = lft

    invert_tree(tree.left)
    invert_tree(tree.right)

tree = BinaryTree.create([1, 2, 3])
tree.print()
invert_tree(tree)
tree.print()
