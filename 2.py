"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p1, p2, curr = l1, l2, dummy_head
        carry = 0
        while p1 != None or p2 != None:
            x = p1.val if p1 != None else 0
            y = p2.val if p2 != None else 0
            new_val = x + y + carry 
            carry = new_val // 10
            curr.next = ListNode(new_val % 10)
            curr = curr.next
            p1 = p1.next if p1 != None else None
            p2 = p2.next if p2 != None else None
        if carry:
            curr.next = ListNode(carry)
        return dummy_head.next