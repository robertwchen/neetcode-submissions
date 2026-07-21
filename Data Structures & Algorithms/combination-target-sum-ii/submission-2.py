# at number [1, 1, 2] # target 4 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # try 
        candidates.sort()
        result = []
        comb = []
        def dfs(i, current_sum):
            if current_sum == target:
                result.append(comb.copy())
                return
            if i >= len(candidates):
                return
            if current_sum > target:
                return
            
            comb.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, current_sum)

        dfs(0, 0)
        return result
            

