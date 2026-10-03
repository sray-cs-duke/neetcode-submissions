class Solution:
    def diameterOfBinaryTree(self, root):

        def dfs(node):
            if node is None:
                return 0, 0

            left_diameter, left_height = dfs(node.left)
            right_diameter, right_height = dfs(node.right)

            current_diameter = left_height + right_height

            best_diameter = max(
                left_diameter,
                right_diameter,
                current_diameter
            )

            current_height = 1 + max(left_height, right_height)

            return best_diameter, current_height

        diameter, height = dfs(root)

        return diameter