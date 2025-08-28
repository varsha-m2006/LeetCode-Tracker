#PROBLEM 124 - BT
#MAXIMUM PATH SUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        #dfs traversal
        def dfs(root):

            #empty
            if not root:
                return 0

            #maxium sum through both paths
            left=max(dfs(root.left),0)
            right=max(dfs(root.right),0)

            #maximum sum
            self.max_sum=max(self.max_sum,left+root.val+right)

            
            return root.val + max(left,right)
        dfs(root)
        return self.max_sum
        
        