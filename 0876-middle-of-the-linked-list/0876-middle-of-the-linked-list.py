# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c=0
        d=0
        current=head
        while(current is not None):
            c+=1
            current=current.next
        if(c%2==0):
            l=(c/2)+1
        else:
            l=round(float(c)/2)
        temp=head
        while(temp is not None):
            d+=1
            if(d==l):
                return temp
            else:
                temp=temp.next
