class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # define need to check
        # define current window
        need = Counter(s1)
        window = Counter()
        
        k = len(s1)
        p1 = 0
        for p2 in range(0, len(s2)):
            window[s2[p2]] += 1
            
            window_len = p2 - p1 + 1
            if window_len > k:
                window[s2[p1]] -= 1
                p1 += 1

            if need == window:
                return True
        return False
                


        