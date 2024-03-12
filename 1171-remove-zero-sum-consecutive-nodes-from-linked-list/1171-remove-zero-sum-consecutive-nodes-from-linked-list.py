class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        temp = head
        while temp:
            res.append(temp.val)
            temp = temp.next
        
        i = 0
        while i < len(res):
            sublist_sum = 0
            for j in range(i, len(res)):
                sublist_sum += res[j]
                if sublist_sum == 0:
                    res = res[:i] + res[j+1:]
                    break
            else:
                i += 1

        new_head = ListNode(0)
        current = new_head
        for val in res:
            current.next = ListNode(val)
            current = current.next
        
        return new_head.next