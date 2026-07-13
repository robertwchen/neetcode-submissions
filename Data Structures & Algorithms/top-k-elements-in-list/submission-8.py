
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        heap = []
        # for num in freq:
            # add (freq, num) sort by -freq

        for num in freq:
            count = freq[num]
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for count, num in heap:
            result.append(num)
        return result



        