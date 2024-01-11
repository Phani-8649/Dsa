# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        c=0
        current=head
        while(current):
            c+=1
            current=current.next
        if(c==1):
            return None
        if(n==1):
            print("1")
            current=head
            for _ in range(c-2):
                current=current.next
            current.next=None
        elif(n==c):
            print("2")
            temp=head.next
            head.next=None
            head=temp
        else:
            print("4")
            current=head
            for _ in range(c-n-1):
                current=current.next
            if(current and current.next):
                current.next=current.next.next
        return head
        

