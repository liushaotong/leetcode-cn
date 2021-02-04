#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        l = ['','', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def dfs(tmp, index):
            if index == len(digits):
                ans.append(tmp)
                return
            letters = l[int(digits[index])]
            for i in letters:
                dfs(tmp+i, index+1)
        dfs('', 0)
        return ans
# @lc code=end

