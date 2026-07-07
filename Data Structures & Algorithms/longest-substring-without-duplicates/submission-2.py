class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a seen set with sliding window
        seen = set()
        max_len = 0

        p1 = 0
        p2 = 1

        for p2 in range(0, len(s)):
            # if seen then move p1 until find the current_char then pop
            current_char = s[p2]
            while current_char in seen:
                    seen.remove(s[p1])
                    p1 += 1
 
            
            max_len = max(max_len, p2 - p1 + 1)
            seen.add(s[p2])


        return max_len

            