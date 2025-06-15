from BTree_Lib import BinaryTree
# The crux of this algorithm is to use a function called 'left_right_highest()' that
# returns the max length from left child, where it would take the max of the left of left child,
# and max length from the right child, where it would take the max of right of left child,
# and vice versa for right child, adding 1 since we are calculating from one depth closer.
# And then we return both of these as a tuple
def left_right_highest(tree: BinaryTree) -> tuple[int, int]:
    leftMax, rightMax = 0, 0
    if tree.left is not None and tree.left.val is not None: # if the left node is 'valid'
        # taking the max of left child result and right child result of left node
        leftMax = max(left_right_highest(tree.left)) + 1
    if tree.right is not None and tree.right.val is not None: # if the right node is 'valid'
        # taking the max of left child result and right child result of right node
        rightMax = max(left_right_highest(tree.right)) + 1

    return (leftMax, rightMax)

def diameter_of_a_tree(tree: BinaryTree) -> int:
    left, right = left_right_highest(tree)
    return left + right # just returning the sum of these length to be the highest path

#tree = BinaryTree.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
#tree.print()
#print(diameter_of_a_tree(tree))
