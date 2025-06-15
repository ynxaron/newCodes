from BTree_Lib import BinaryTree as BT
# The crux of this algorithm is to use the idea that the solution
# of bt_maximum_path(tree) is max_of bt_max tree.left, bt_max tree.right
# and, this is important, max of maximum value that could be taken from tree.left,
# maximum value from tree.right, and the addition of this two + tree.val. Let me explain:
#
# The answer to our current node is either in left node or right node, or a seperate path
# that takes the maximum node value (by taking a path) from left node, maximum node value
# from right node, and then taking the max of left_max, right_max, or just combining these
# with tree.val. These 'means', if tree.val is negative enough to offset the max of left path
# and right path, then we take max of either those, or else we take sum of left max,
# left max + tree.val + right max, and right max
def bt_maximum_path(tree: BT | None) -> int:
    # if this subtree is invalid, then we simply return 0, meaning not taking
    if tree is None or tree.val is None:
        return 0

    # lmax, rmax are the maximum value from a path from a left node, and a right node
    lmax, rmax = tree.left.maximum_value(), tree.right.maximum_value()
    # this_val means taking the max of left value, right value, or walking the path from left val and right val
    this_val = max(lmax, lmax + tree.val + rmax, rmax)

    # and this is just taking the left subtree answer, right subtree answer, and this_val
    lans, rans = bt_maximum_path(tree.left), bt_maximum_path(tree.right)
    return max(lans, this_val, rans)

# tree = BT.create([-1, 2, 3, -4, 5, 6, -4, 5, -8])
# tree.print()
# print(bt_maximum_path(tree))

#             -1
#            /   \
#           2     3
#          / \   / \
#        -4  5  6  -4
#        / \
#       5  -8
