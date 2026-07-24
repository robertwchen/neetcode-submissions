class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            max_len = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    cur_len = dfs(j, memo)
                    max_len = max(cur_len, max_len)
            memo[i] = 1 + max_len
            return memo[i]

        max_len = 0
        for i in range(len(nums)):
            cur_len = dfs(i, memo)
            max_len = max(cur_len, max_len)
        return max_len
                    
                    
            
