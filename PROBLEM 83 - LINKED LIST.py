#PROBLEM 83 - LINKED LIST
#REMOVE DUPLICATES FROM SORTED LIST

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#unlike the mdeium version here u juist have to remove the duplicates not the lement that has the duplicate as well
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        seen = set()
        curr = head
        prev = None

        while curr:
            if curr.val in seen:
                #deletion
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next
        
        return head

        