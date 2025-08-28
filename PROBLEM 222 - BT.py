#PROBLEM 222 - BT
#COUNT COMPLETE TREE NODES

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #if empty
        if not root:
            return 0
        
        #DFS traversal
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        
        #returning no of nodes
        return 1+left+right


        