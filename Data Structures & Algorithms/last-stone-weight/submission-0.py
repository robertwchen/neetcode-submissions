# where am I
    # at list smashing stones shrinking
# what am I doing
    # I am going to smash the heaviest stones and shrink the array
# what do I return
    # return last stone 

# [w1, w2, w3]
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max_heap
        # define max heap -> (-weight, index)
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, (-stone, stone))
        print(max_heap)

        while len(max_heap) > 1:
            # pop top 2 max elements from heap
            stone1 = heapq.heappop(max_heap)[1]
            stone2 = heapq.heappop(max_heap)[1]
            print(f"stone1: {stone1} stone2:{stone2}")
            
            if stone1 == stone2:
                continue
            else:
                stone_left = abs(stone1 - stone2)
                heapq.heappush(max_heap, (-stone_left, stone_left))

            # if same then pop both
            # if different pop minimun pop maximun 
                # subtract by minimum and push back on

        if max_heap:
             return max_heap[0][1]
        else:
            return 0
        # 
        