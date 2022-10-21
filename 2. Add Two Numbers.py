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
        l3 = ListNode(0)
        carry = 0
        curr = l3
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
                
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            sum_ = l1_val + l2_val + carry
            
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            carry = sum_ // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
            
        return l3.next
