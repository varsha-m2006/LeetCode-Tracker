#PROBLEM 543 - BT
#DIAMETER OF BINARY TREE

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        #diameter
        self.longest=0

        #dfs traversal
        def dfs(root):
            #if empty
            if not root:
                return 0
            
            #path through both directions
            left=dfs(root.left)
            right=dfs(root.right)

            #maximum diameter 
            self.longest=max(self.longest,left+right)

            #maximum  path
            return 1+ max(left,right)
        dfs(root)
        return self.longest
        