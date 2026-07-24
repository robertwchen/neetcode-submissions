# 'A' 'B' 'C'   'Z'
# '1' '2' '3'.  '26'




# 104
# i
class Solution:
    def numDecodings(self, s: str) -> int:
        return self._numDecodings(s, 0, {})
        
    def _numDecodings(self, s, i, memo) -> int:
        
        if i in memo:
            return memo[i]

        if i == len(s):
            return 1

        if int(s[i]) == 0:
            return 0

        take_one = self._numDecodings(s, i + 1, memo)
        take_two = 0
        if i + 2 <= len(s) and int(s[i:i + 2]) <= 26:
            take_two = self._numDecodings(s, i + 2, memo)
        
        memo[i] = take_one + take_two
        return memo[i]
        
        
