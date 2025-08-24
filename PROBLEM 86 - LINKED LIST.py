#PROBLEM 86 - LINKED LIST
#PARTITION LIST

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        #creating dummies for both partitions
        r_l = ListNode(0)
        r = r_l
        l_l=ListNode(0)
        l=l_l

        curr = head
        #first pass: nodes < x
        while curr:
            if curr.val < x:
                r.next = curr
                r = r.next
            if curr.val >= x:
                l.next = curr
                l = l.next
            curr = curr.next
        
        #adding head of second partition to the end of the first one
        r.next=l_l.next
        l.next=None

        return r_l.next

        


       
            

        
        