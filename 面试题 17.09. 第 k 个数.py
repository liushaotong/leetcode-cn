class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        seq=set()
        heap=[]
        heapq.heappush(heap,1)
        while 1:
            cur=heapq.heappop(heap)
            if not cur in seq:
                seq.add(cur)
                for factor in [3,5,7]:
                    heapq.heappush(heap,cur*factor)
            if (len(seq)==k):
                return cur