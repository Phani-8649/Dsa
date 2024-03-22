# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode()  # Dummy node to keep track of the result linked list
        current = dummy_head     # Pointer to iterate through the result linked list
        carry = 0                # Variable to keep track of the carry

        while l1 or l2 or carry:
            # Calculate the sum of current digits and the carry
            sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            
            # Update the carry
            carry = sum_val // 10
            
            # Create a new node with the sum modulo 10
            current.next = ListNode(sum_val % 10)
            current = current.next
            
            # Move to the next nodes in the input lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next  # Return the next node of the dummy node, which is the head of the result list
