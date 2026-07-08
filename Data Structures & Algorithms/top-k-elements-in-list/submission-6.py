import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort idea:
        bucket = [[] for _ in range(0, len(nums) + 1)] 
        freq = Counter(nums)

        # have array index = freq val = set(nums)
        for n in freq:
            print(len(bucket), freq[n])
            bucket[freq[n]].append(n)


        # loop through from end of bucket to beginning 
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                result.append(n)
            if len(result) == k:
                return result
        return []


        

        



