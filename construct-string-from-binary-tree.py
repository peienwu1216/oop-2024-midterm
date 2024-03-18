from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Create a string representation of a binary tree following specific formatting rules.

        The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:
        - Node Representation: Each node in the tree should be represented by its integer value.
        - Parentheses for Children: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:
            - If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node's value.
            - If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.
        - Omitting Empty Parentheses: Any empty parentheses pairs (i.e., ()) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            str: The string representation of the binary tree based on the specified rules.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> root1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
            >>> solution.tree2str(root1)
            '1(2(4))(3)'

            # Example 2:
            >>> root2 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
            >>> solution.tree2str(root2)
            '1(2()(4))(3)'
        """
        def pre_order(root):
            if root is None: 
                return ''
            
            proc_str = ''
            if root.right:
                proc_str += f'({pre_order(root.left)})({pre_order(root.right)})'
            else:
                proc_str += f'({pre_order(root.left)})' if root.left is not None else ''
            
            return str(root.val) + proc_str

        return pre_order(root)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    