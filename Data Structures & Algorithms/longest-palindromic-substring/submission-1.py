# where am I
    # at some c on string
# what am I doing
    # check if 
# what do I return


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        for i in range(0, len(s)):
            odd_str = self.palin_len_odd(s, i)
            even_str = self.palin_len_even(s, i)
            max_str = odd_str if len(odd_str) > len(max_str) else max_str
            max_str = even_str if len(even_str) > len(max_str) else max_str
        return max_str
    
    def palin_len_odd(self, s, start_index):
        p1 = start_index - 1
        p2 = start_index + 1
        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            else:
                break
        return s[p1 + 1:p2]

    def palin_len_even(self, s, start_index):
        p1 = start_index
        p2 = start_index + 1
        while p1 >= 0 and p2 < len(s):
            if s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            else:
                break
        return s[p1 + 1:p2]
        
            
#sol = Solution()
#s = "ababd"
#print(sol.palin_len_odd(s,1))

        
        