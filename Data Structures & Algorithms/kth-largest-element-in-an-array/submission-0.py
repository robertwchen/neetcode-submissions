# where am I
    # some number on array
# what am I doing
    # pushing and popping elements
# what do I return
    # kth sized element

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap to pop minimum to maintain maxes 
        if len(nums) == 0:
            return 0

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

        