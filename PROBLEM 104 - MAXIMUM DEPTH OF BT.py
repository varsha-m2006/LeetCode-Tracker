#PROBLEM 104 - MAXIMUM DEPTH OF BT
#MAXIMUM DEPTH OF BINARY TREE

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        #which side has more depth is the max depth of the tree
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        