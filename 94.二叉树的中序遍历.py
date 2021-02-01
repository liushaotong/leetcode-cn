#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []

        while stack or root:
            if root:
                # 这部分将左子树压入栈中
                stack.append(root)
                root = root.left
            else:
                # 进入右子树前处理值
                tmp = stack.pop()
                ans.append(tmp.val)
                # 进入右子树，继续循环
                root = tmp.right  #是tmp的右子树而不是root的，因为root是空节点了
            
        return ans

# @lc code=end

