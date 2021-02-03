#
# @lc app=leetcode.cn id=621 lang=python
#
# [621] 任务调度器
#

# @lc code=start
import collections
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        queue = []
        time = 0
        remain_counter = collections.Counter(tasks)
        for i in remain_counter:
            heapq.heappush(queue, -remain_counter[i])
        while queue:
            i = 0
            tmp = []
            while i <= n:
                if queue:
                    value = heapq.heappop(queue)
                    #value = abs(heapq.heappop(queue))
                    value = abs(value)
                    if value > 1:
                        tmp.append(value-1)
                time += 1
                if not queue and len(tmp) == 0:
                    break
                i += 1
            for item in tmp:
                heapq.heappush(queue, -item)
        return time

# @lc code=end

