class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if hash s = hash t
        return (self.counter(s) == self.counter(t))

    def counter(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        return count       
        