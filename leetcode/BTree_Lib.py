class BinaryTree:
    # initializing a binary tree with the capibility to have no values, no left or right child
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    # the crux of printing algorithm is to use a queue such that we print the values of
    # current tree, then append to the right, if available, it's left child, if available it's
    # right child, and then pop this value that we have appended
    def print(self):
        print(self.to_string())

    # using a 'padding' variable such that it represents roughly the length
    # of the last level (that would ultimately decide shape of the tree)
    def to_string(self) -> str:
        padding = " " * (
            2 ** (self.height() + 1)
        )  # the appropriate space in between each nodes
        this_queue = [self]
        return_str = ""
        while this_queue != []:  # while there are elements to be printed
            this_str = ""  # in where our values would be appended
            new_queue = []
            for node in this_queue:
                if node.val is not None:
                    this_str += padding + str(node.val)
                    if node.left is not None:
                        new_queue.append(node.left)
                    if node.right is not None:
                        new_queue.append(node.right)
            padding = padding[
                : len(padding) // 2
            ]  # halving the padding each level that we passes
            return_str += this_str + "\n"
            this_queue = new_queue
        return return_str

    @staticmethod
    # the crux of the creating algorithm is to use a queue as well, iterating over the values
    # and appending to the right a left child and a right child
    def create(init: list[int | None]):
        return_tree = BinaryTree()
        tree_queue = [return_tree]
        for val in init:
            tree = tree_queue.pop(0)
            tree.val = val
            tree.left = BinaryTree()
            tree.right = BinaryTree()
            # this will work because at any time we would only have nodes in a single level,
            # and we would go a level down only after all nodes in the current level have been
            # exhausted
            tree_queue.append(tree.left)  # appending left
            tree_queue.append(tree.right)  # appending right
        return return_tree

    # The crux of this algorithm is to use take the max height that came from left child, right child,
    # add 1 to that max and return that. Since the maximum depth node is either in left child or right child
    # this works, and since we have answer from one level lower, we must add 1 to the answer
    def height(self) -> int:
        leftHeight, rightHeight = 0, 0
        if (
            self.left is not None and self.left.val is not None
        ):  # checking if 'left' node is valid
            leftHeight = self.left.height()
        if (
            self.right is not None and self.right.val is not None
        ):  # checking if 'right' node is valid
            rightHeight = self.right.height()
        return (
            max(leftHeight, rightHeight) + 1
        )  # compensating since we searched from one depth lower

    # This function checks for equality by checking if each node is equal to the other
    # THIS FUNCTION IS NOT WORKING
    def equal(self, another) -> bool:
        if self.val is None and another.val is None:
            return True
        if self.val is None or another.val is None:
            return False
        if self.val == another.val:
            return self.left.equal(another.left) and self.right.equal(another.right)
        return False

    # This function converts a tree to a sorted array. First it appends all values
    # at the left subtree, appends value at current node, then appends all value at
    # a right subtree.
    def to_inorder(self) -> list[int]:
        def helper(tree, array: list[int]):
            if tree.left is not None:
                helper(tree.left, array)
            if tree.val is not None:
                array.append(tree.val)
            if tree.right is not None:
                helper(tree.right, array)

        array = []
        helper(self, array)
        return array

    # This function concerts a tree to a preorder path, which first appends current value
    # then goes to left subtree, then goes to right subtree
    def to_preorder(self) -> list[int]:
        def helper(tree, array: list[int]):
            if tree.val is not None:
                array.append(tree.val)
            if tree.left is not None:
                helper(tree.left, array)
            if tree.right is not None:
                helper(tree.right, array)

        array = []
        helper(self, array)
        return array

    # This returns the maximum value that could be taken from a tree
    def maximum_value(self) -> int:
        # if subtree is None, simply return 0
        if self is None or self.val is None:
            return 0
        # consider left and right value if sum is positive
        l = max(self.left.maximum_value(), 0)
        r = max(self.right.maximum_value(), 0)
        # see if adding the current tree.val, a possible negative value
        # would make the total sum less than 0. Discard if it does
        return max((self.val + max(l, r)), 0)
