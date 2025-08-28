#PROBLEM 98 - BT
#VALIDATE BINARY SEARCH TREE

class Solution(object):
    def isValidBST(self, root):

        def validate(node, low, high):

            #if empty
            if not node:
                return True
            
            #if rule satisfies
            if not (low < node.val < high):
                return False
            
            #recursive call
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float("-inf"), float("inf"))
