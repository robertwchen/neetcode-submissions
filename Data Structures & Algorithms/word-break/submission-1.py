# where am I
    # at some point on the word
# what am I doing
# what do I return

#s = "hello"
#dict = ["hel", "lo"] 
#.       p
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # move p2 up until find char then reset p1 
        wordSet = set(wordDict)
        return self._wordBreak(s, wordSet, {})

    def _wordBreak(self, s, wordSet, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return True

        ptr = 0 # represents last element we take
        for ptr in range(len(s)):
            if s[:ptr + 1] in wordSet:
                if self._wordBreak(s[ptr + 1:], wordSet , memo): # from next char after ptr
                    memo[s] = True
                    return memo[s]
        memo[s] = False
        return memo[s]