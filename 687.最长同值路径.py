#
# @lc app=leetcode.cn id=687 lang=python
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def length(node):
            if not node:
                return 0
            else:
                left_length = length(node.left)
                right_length = length(node.right)
                max_length = 0
                if node.left != None and node.left.val == node.val and node.right != None and node.right.val == node.val:
                    self.ans = max(self.ans, left_length+right_length+2)
                if node.left != None and node.left.val == node.val:
                    max_length = left_length + 1
                if node.right != None and node.right.val == node.val:
                    max_length = max(max_length, right_length+1)
                self.ans = max(self.ans, max_length)
                return max_length
        length(root)
        return self.ans
# @lc code=end

