#PROBLEM 236 - BT
#LCA

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        #if empty or you rech p or q
        if not root or root==p or root==q:
            return root

        #DFS traversal
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        #common ancestor 
        if left and right:
            return root
        else:
            return left or right


        