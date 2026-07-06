import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            heap.append((-count, num))

        heapq.heapify(heap)
        result = []
        
        for i in heap[:k]:
            count, num = heapq.heappop(heap)
            result.append(num)

        return result




