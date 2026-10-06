from collections import deque

class Solution:
    def buildTree(self, preorder, inorder):
        preorder_queue = deque(preorder)

        positions = {}

        for i in range(len(inorder)):
            positions[inorder[i]] = i

        def build(left, right):
            if left > right:
                return None

            root_value = preorder_queue.popleft()
            root = TreeNode(root_value)

            middle = positions[root_value]

            root.left = build(left, middle - 1)
            root.right = build(middle + 1, right)

            return root

        return build(0, len(inorder) - 1)