#PROBLEM 19 - LINKED LIST
#REMOVE NTH NODE FROM END OF LIST

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr=head

        #length is initialized to 0
        c=0

        #calculating length
        while curr:
            c+=1
            curr=curr.next
        
        #finding position
        pos=c-n

        i=0

        #if the node to delete is the first node(head)
        if pos==0:
            return head.next

        curr2=head#just a temporary pointer to walk through the list

        #moving to node before the node we need to delete
        while i<pos-1:
            curr2=curr2.next
            i+=1
            
        #deletion by re-linking
        curr2.next=curr2.next.next

        return head#return head as that is the actual list