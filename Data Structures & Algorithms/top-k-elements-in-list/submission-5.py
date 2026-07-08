import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a minheap
        # build freq map
        freq = Counter(nums)
        heap = []

        for n in freq:
            heapq.heappush(heap, (freq[n], n))
        
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for count, n in heap]
        



