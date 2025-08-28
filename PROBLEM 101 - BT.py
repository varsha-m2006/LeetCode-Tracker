#PROBLEM 101 - BT
#SYMMETRIC TREE

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mirror(t1,t2):

            #if both are empty
            if not t1 and not t2:
                return True

            #if either one of them is empty
            if not t1 or not t2:
                return False

            #if values are not equal
            if t1.val != t2.val:
                return False

            #recursive call
            return mirror(t1.left, t2.right) and mirror(t1.right, t2.left)

        return mirror(root.left, root.right)