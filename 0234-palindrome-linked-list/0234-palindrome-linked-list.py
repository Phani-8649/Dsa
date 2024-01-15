# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast=head
        slow=head


        #find middle(slow pointer will go there)
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #reverse second half
        #without reversing shift fast->slow and slow->head then it is same like reversing and then traverse throught the list
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        #check palindrone
        left,right=head,prev
        while right:
            if(left.val !=right.val):
                return False
            left=left.next
            right=right.next
        return True
        