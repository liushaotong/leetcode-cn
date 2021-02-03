#
# @lc app=leetcode.cn id=933 lang=python
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while self.queue[0] < self.queue[-1] -3000:
            self.queue.pop(0)
        return len(self.queue)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

