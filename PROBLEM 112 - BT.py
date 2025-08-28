#PROBLEM 112 - BT
#PATH SUM

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        #if empty
        if not root:
            return False

        
        def cal(root,sum):

            #if empty
            if not root:
                return False

            #adding value of each node
            sum+=root.val

            #checking if we are at leaf nodes, and sum is equal to the target
            if root.left is None and root.right is None and sum==targetSum:
                return True

            #recursive call
            return cal(root.left,sum) or cal(root.right,sum)
        return cal(root,0)
        

        