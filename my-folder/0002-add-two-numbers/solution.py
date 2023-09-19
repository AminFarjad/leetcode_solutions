# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        start = res
        carry = 0
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = int(temp/10)
            temp = temp % 10
            res.next = ListNode(temp) 
            l1 = l1.next
            l2 = l2.next
            res = res.next
        while l1 != None:
            temp = l1.val + carry
            carry = int(temp/10)
            temp = temp % 10
            res.next = ListNode(temp) 
            l1 = l1.next
            res = res.next

        while l2 != None:
            temp = l2.val + carry
            carry = int(temp/10)
            temp = temp % 10
            res.next = ListNode(temp) 
            l2 = l2.next
            res = res.next

        if carry != 0:
            res.next = ListNode(carry)
        
        return start.next

