from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)
        for s in strs:
            s_tuple = tuple(self.string_to_list(s))
            anagrams[s_tuple].append(s)
        
        for anagram in anagrams:
            result.append(anagrams[anagram])
        return result

    def string_to_list(self, s):
        s_list = [0] * 26
        for c in s:
            ascii = ord(c) - ord('a')
            s_list[ascii] += 1
        return s_list
"""
s1 = "white"
s2 = ""
strs = ["act","pots","tops","cat","stop","hat"]

sol = Solution()
print(sol.string_to_list(s1))
print(sol.string_to_list(s2))
print(sol.groupAnagrams(strs))
"""