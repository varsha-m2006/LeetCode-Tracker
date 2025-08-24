#PROBLEM 21 - LINKED LIST
#MERGE TWO SORTED LISTS

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = list1
        curr2 = list2

        # dummy node to start the new list
        dummy = ListNode()
        curr = dummy

        #add the elements from each of the lists in order
        while curr1 or curr2:
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:
                    curr.next = ListNode(curr1.val)
                    curr1 = curr1.next
                else:
                    curr.next = ListNode(curr2.val)
                    curr2 = curr2.next
            elif curr1:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next

            curr = curr.next  #move curr forward

        return dummy.next  #return head of merged list

            
            

        