#PROBLEM 234 - LINKED LIST
#PALINDROME LINKED LIST

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        #copy list into new
        new = ListNode(head.val)#directly added the first value here isntead of having this as a default 0 and then starting head from the next node, so comparison is easier
        curr1 = new
        curr2 = head.next


        while curr2:
            curr1.next = ListNode(curr2.val)  #create new node
            curr1 = curr1.next
            curr2 = curr2.next

        #reverse original
        curr3 = head
        prev = None
        while curr3:
            nxt = curr3.next
            curr3.next = prev
            prev = curr3
            curr3 = nxt

        #compare reversed original (prev) with copy (new)
        curr4 = new
        curr5 = prev
        while curr5:
            if curr4.val != curr5.val:
                return False
            curr4 = curr4.next
            curr5 = curr5.next

        return True


                

        