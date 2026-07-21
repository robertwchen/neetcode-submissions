class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        first = nums[0]
        perms = self.permute(nums[1:])

        all_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                all_perms.append(p[:i] + [first] + p[i:])
        return all_perms

        
