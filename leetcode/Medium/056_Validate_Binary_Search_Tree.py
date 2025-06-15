from BTree_Lib import BinaryTree as BT
# The crux of this algorithm depends upon us figuring out that to verify each
# node we need to have a leftLimit, and a rightLimit, that would tell us at each
# node test whether this value is greater than the leftLimit and smaller than the
# rightLimit, or not. If true, then we call this function again, but with updated
# limits. When testing the left branch, now all the nodes need to be smaller than
# this current node value, hence we update our rightLimit, and when testing the
# right branch, all the nodes need to be bigger than our current node value, hence
# we update our leftLimit.
def validate_binary_search_tree(tree: BT | None) -> bool:
    # creating a helper function with a bit more complicated signature, taking in
    # our initial left and right limits.
    def helper(leftLimit: int | float, tree: BT | None, rightLimit: int | float) -> bool:
        # if it touches the base cases, simply return true
        if tree is None or tree.val is None:
            return True

        # if the condition are satisfied
        if leftLimit < tree.val and tree.val < rightLimit:
            # return with, for left branch, our rightLimit updated, and for right branch our leftLimit updated
            return helper(leftLimit, tree.left, tree.val) and helper(tree.val, tree.right, rightLimit)
        else:
            # else just return False
            return False

    # initiating the helper function with negative and positive inf, to ensure the first case, the root node, passes
    return helper(-float("inf"), tree, float("inf"))

# tree = BT.create([6, 4, 8, 2, 5, 7, 9])
# tree.print()
# print(validate_binary_search_tree(tree))
