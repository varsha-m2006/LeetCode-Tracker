#PROBLEM 100 - BT
#SAME TREE

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        #if both are empty
        if not p and not q:
            return True

        #if one of them is empty
        if not p or not q:
            return False

        #if value is not equal
        if p.val!=q.val:
            return False

        #moving left and moving right then comparing through recursive call
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        