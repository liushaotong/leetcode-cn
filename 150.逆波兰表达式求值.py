#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                tmp = stack.pop()
                stack.append(stack.pop()-tmp)
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            elif i == '/':
                b = stack.pop()
                a = stack.pop()
                if a*b>=0:
                    stack.append(a/b)
                else:
                    stack.append(-(-a/b))
            else:
                stack.append(int(i))
        return stack[0]

# @lc code=end

