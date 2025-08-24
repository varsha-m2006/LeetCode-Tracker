#PROBLEM 82 - LINKED LIST
#REMOVE DUPLICATES FROM SORTED LIST II

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #hashmap for calculating frequencies
        seen={}
        curr=head

        #incrementing the no. of frequencies
        while curr:
            if curr.val in seen:
                seen[curr.val]+=1
            else:
                seen[curr.val]=1
            curr=curr.next
        
        #list of duplicate elements
        l=[]
        
        #addong the duplicate items 
        for k,v in seen.items():
            if seen[k]>1:
                for i in range(v):
                    l.append(k)
        
        #deleting
        for i in l:
            curr1=head
            prev=None
            while curr1.val!=i:
                prev=curr1
                curr1=curr1.next
            #if not head
            if curr1 is not head:
                prev.next=curr1.next
            #if head, then make next node new head
            else:
                curr1=curr1.next
                head=curr1
                  
        return head

        