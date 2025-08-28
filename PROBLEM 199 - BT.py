#PROBLEM 199 - BT
#BINARY TREE RIGHT SIDE VIEW

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        #bfs traversal, level checking
        output = []
        q = deque([root])

        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                
                #take the last node of each level
                if i == level_length - 1:
                    output.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return output
