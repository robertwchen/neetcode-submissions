from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = Counter()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]

            complements[num] = i 
        