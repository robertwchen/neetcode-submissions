class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map of complements
        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in complements:
                return [complements.get(complement), i]
            complements[nums[i]] = i
        # find complement
        # check if in complement hash map
        # if not store it and move on
        