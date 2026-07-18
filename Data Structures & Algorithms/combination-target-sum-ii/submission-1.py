# where am I
    # at some number on the candidates
# what am I doing
    # I try without then try with each element
# what do I return
    # if find target == 0
    # or if len(candidates) == 0
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def _combinationSum2(candidates, target, i):
            if target == 0:
                return [[]]

            if target < 0:
                return []
            
            if i == len(candidates):
                return []
            
        
            # try without element
            first_candidate = candidates[i]
            next_i = i + 1
            while next_i < len(candidates) and candidates[i] == candidates[next_i]:
                next_i += 1
            without_first_candidate = _combinationSum2(candidates, target, next_i) # returns me all possible combinations without it

            all_candidates = []
            with_first_candidate = _combinationSum2(candidates, target - first_candidate, i + 1)
            for comb in with_first_candidate:
                all_candidates.append([first_candidate, *comb])
            return all_candidates + without_first_candidate
        return _combinationSum2(candidates, target, 0)



        