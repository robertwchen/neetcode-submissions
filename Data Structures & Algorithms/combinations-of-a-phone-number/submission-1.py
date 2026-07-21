# where am I
    # at some letter generate all permutations
# what am I doing
# what do I return

#2 3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        all_perms = []
        perm = []
        def dfs(i):
            if i == len(digits):
                all_perms.append("".join(perm))
                return 
            letters = digit_map[int(digits[i])]
            
            for c in letters:
                perm.append(c)
                dfs(i + 1)
                perm.pop()
        dfs(0)
        return all_perms




            
                
        