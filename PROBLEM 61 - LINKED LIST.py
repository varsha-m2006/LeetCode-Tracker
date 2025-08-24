#PROBLEM 61 - LINKED LIST
#ROTATE LIST

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        #if empty list or list with only one node or number of rotations is 0
        if not head or not head.next or k == 0:
            return head

        curr1=head

        #calculating length
        length=0
        while curr1:
            curr1=curr1.next
            length+=1
        
        #number of rotations incase k is greater than length
        if k>length:
            k=k%length
        
        #rotation
        for i in range(k):

            #initialize everytime
            curr=head
            prev=None

            #move to last node
            while curr.next:
                prev=curr
                curr=curr.next
            
            #make last node the head
            curr.next=head
            prev.next=None
            head=curr
            
        return head
