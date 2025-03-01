# LeetCode Mode:

from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node):
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if abs(height(node.left) - height(node.right)) > 1:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return True