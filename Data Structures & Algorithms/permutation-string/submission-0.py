class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()

        p1 = 0
        k = len(s1)
        for p2 in range(0, len(s2)):
            # always increment p2 
            char = s2[p2]
            window[char] += 1
            
            window_size = p2 - p1 + 1
            if window_size > k:
                window[s2[p1]] -= 1
                p1 += 1

            if window == need:
                return True
        return False
                


        