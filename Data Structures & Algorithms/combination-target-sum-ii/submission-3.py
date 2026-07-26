# where am I
    # at some point on array
# what am I doing
    # deciding if I wnat this elemetn or not
# what do I return 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        candidates.sort()

        def dfs(i, target):
            if target == 0:
                result.append(comb.copy())
                return
            if target < 0:
                return
            if i >= len(candidates):
                return 
            
            current = candidates[i]
            comb.append(current)
            dfs(i + 1, target - current)
            comb.pop()

            while i < len(candidates) and candidates[i] == current:
                i += 1
            
            dfs(i, target)
        dfs(0, target)
        return result



