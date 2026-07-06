import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basically make a counter first
        count = {}

        freq = []
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        for i in range(0, len(nums) + 1):
            freq.append([])
        # freq array where freq is index and value is added to  list in array
        for n in count:
            n_count = count[n]
            freq[n_count].append(n)
        print(freq)

        result = []

        for i in range(len(freq) - 1, -1, -1):

            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
            
        return result



