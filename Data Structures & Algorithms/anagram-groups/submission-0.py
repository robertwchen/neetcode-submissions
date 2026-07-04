from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have map: key -> [alpha_list]  val -> ["anagram1", "anagram2"]
        # loop through strings:
        anagram_map = defaultdict(list)
        for s in strs:
            s_tuple = self.alpha_list(s)
            anagram_map[s_tuple].append(s)
            
        result = []
        for anagram in anagram_map:
            result.append(anagram_map[anagram])

        return result
    
    def alpha_list(self, alpha_string):
        alpha_list = [0] * 26
        for c in alpha_string:
            index = ord(c) - ord('a') 
            alpha_list[index] += 1

        return tuple(alpha_list)
