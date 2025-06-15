from BTree_Lib import BinaryTree
# we are simply checking if each node of the two binary trees are the same value or not
def same_tree(l: BinaryTree, r: BinaryTree) -> bool:
    # checking if both are None, return True
    if l is None and r is None:
        return True
    # if one is None and other not, or vals don't match
    if l is None or r is None or (l.val != r.val):
        return False
    # else just returning if both left subtree and right subtree match
    return same_tree(l.left, r.left) and same_tree(l.right, r.right)
