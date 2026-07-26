# where am I
    # at some window on array
# what am I doing
# what do I return

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # set up the deque
        queue = deque([])
        result = []

        left = 0
        for right in range(len(nums)):
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)  

            if queue[0] < left:
                queue.popleft()
            # process next element and remove last
  

            if right >= k - 1:
                result.append(nums[queue[0]])
                left += 1


        return result 


        