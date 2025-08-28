#PROBLEM 1302 - BT
#DEEPEST LEAVES SUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.sum=0
        self.max_depth=0

        #finding max depth
        def maxDepth(root):
            if not root:
                return 0
            return 1+max(maxDepth(root.left),maxDepth(root.right))
        self.max_depth=maxDepth(root)

        #DFS traversal
        def dfs(root,depth):

            #if empty
            if not root:
                return
            
            #if leaf node reached and its at the maximum deoth
            if not root.left and not root.right and depth==self.max_depth:

                #update sum
                self.sum+=root.val
            else:
                #DFS traversal, incrementing depth as u go further down
                dfs(root.left,depth+1)
                dfs(root.right,depth+1)
            
        dfs(root,1)
        return self.sum
        