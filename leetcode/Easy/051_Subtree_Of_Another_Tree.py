from BTree_Lib import BinaryTree as BT
def subtree_of_another_tree(tree: BT | None, subtree: BT | None) -> bool:
    if subtree is None or tree is None:
        return False

    if tree.equal(subtree):
        return True

    return subtree_of_another_tree(tree.left, subtree) or subtree_of_another_tree(tree.right, subtree)
