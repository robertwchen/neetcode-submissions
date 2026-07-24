


# aab
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.count_palindromes(s, i, i)
            if i + 1 < len(s):
                count += self.count_palindromes(s, i, i + 1)
        return count
    
    # asume [aaa] 
    # odd case: start == end
    # even case: end == start + 1
    def count_palindromes(self, s, start, end):
        if s[start] != s[end]:
            return 0
        count = 0
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            count += 1
            start -= 1
            end += 1
        return count