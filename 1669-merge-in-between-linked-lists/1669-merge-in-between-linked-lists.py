# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        c=0
        d=0
        a_add = b_add = None
        temp=current=list1
        # current=list2
        while(temp):
            c+=1
            if(c==a):
                a_add=temp
            elif(c==b+1):
                b_add=temp
            temp=temp.next
        a_add.next=list2
        while list2.next:
            list2 = list2.next
        list2.next = b_add.next
        return list1
