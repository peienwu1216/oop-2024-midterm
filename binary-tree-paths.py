from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Return all root-to-leaf paths in a binary tree in any order.

        A leaf is a node with no children.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[str]: A list of all root-to-leaf paths.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> root1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
            >>> solution.binaryTreePaths(root1)
            ['1->2->5', '1->3']

            # Example 2:
            >>> root2 = TreeNode(1)
            >>> solution.binaryTreePaths(root2)
            ['1']
        """
        answer = []
        def traverse(root, tmp_str=''):
            nonlocal answer
            if root.left is None and root.right is None:
                answer.append(tmp_str)
                return
            
            if root.left is not None:
                traverse(root.left, f'{tmp_str}->{root.left.val}')
            if root.right is not None:
                traverse(root.right, f'{tmp_str}->{root.right.val}')

        traverse(root, str(root.val))
        return answer
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)