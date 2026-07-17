# where am I
     # at some point processing chars sorted by cooldown
# what am I doing
     # I am pushing all letters into the heap with cooldown 0
     # I then decide whether to push it back in or not and increment cooldown
# what do I return
    # when the heap is empty

# mark when I visit node what iteration 


# throw it in a counter
# loop through and basically turn into heap with [ (time_left, frequency, letter)] 

from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 2 heaps cooldown which is minheap 
        # freq heap which is max heap we process chars with max count first
        queue = deque([]) # cooldown sort only
        max_heap = [] # freq sort only
        counts = Counter(tasks)
        cycles = 0

        for letter in counts:
            freq = counts[letter]
            heapq.heappush(max_heap, -freq)
        print(max_heap)

        time = 0
        while max_heap or queue:
            time += 1
            
            if max_heap:
                freq = heapq.heappop(max_heap) + 1
                if freq < 0:
                    queue.append((time + n, freq))
            
            if queue and queue[0][0] == time:
                freq = queue[0][1]
                queue.popleft()
                heapq.heappush(max_heap, freq)
        return time
        




    
        