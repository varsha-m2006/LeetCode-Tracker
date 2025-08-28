#PROBLEM 257 - BT
#BINARY TREE PATHS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        self.output=[]
        def dfs(node, path):
            if not node:
                return
            #adding values in string
            path += str(node.val)

            #if leaf node reached
            if not node.left and not node.right:
                self.output.append(path)

            #dfs traversal
            else:
                dfs(node.left, path + "->")
                dfs(node.right, path + "->")

        dfs(root,"")
        return self.output
            