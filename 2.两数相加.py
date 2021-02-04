#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
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
        def add(a, b, carry):
            if not (a or b):
                return ListNode(1) if carry else None
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            val = a.val + b.val + carry
            carry = 1 if val >= 10 else 0
            a.val = val % 10
            a.next = add(a.next, b.next, carry)
            return a
        return add(l1, l2, 0)
# @lc code=end

