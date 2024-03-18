from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Parameters:
            p (Optional[TreeNode]): The root of the first binary tree.
            q (Optional[TreeNode]): The root of the second binary tree.

        Returns:
            bool: True if the trees are the same, False otherwise.

        Examples:
            >>> solution = Solution()
            >>> p1 = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> q1 = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> solution.isSameTree(p1, q1)
            True

            >>> p2 = TreeNode(1, TreeNode(2), None)
            >>> q2 = TreeNode(1, None, TreeNode(2))
            >>> solution.isSameTree(p2, q2)
            False

            >>> p3 = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(1, None, TreeNode(2)))
            >>> q3 = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(2, None, TreeNode(1)))
            >>> solution.isSameTree(p3, q3)
            False
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)