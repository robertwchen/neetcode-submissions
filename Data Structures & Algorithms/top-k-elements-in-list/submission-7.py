class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        

        # bucket sort:
        bucket = [[] for i in range(len(nums) + 1)]
        for num in freq:
            index = freq[num]
            bucket[index].append(num)

        result = []
        #[[1, 2, 3], [4]]
        # loop through bucket
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        