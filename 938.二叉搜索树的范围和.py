#
# @lc app=leetcode.cn id=938 lang=python
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        else:
            if root.val > high:
                return self.rangeSumBST(root.left, low, high)
            elif root.val < low:
                return self.rangeSumBST(root.right, low, high)
            else:
                return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
# @lc code=end

