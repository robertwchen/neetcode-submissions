class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = Counter(s1)
        window_count = Counter()

        p1 = 0
        for p2 in range(len(s2)):
            window_count[s2[p2]] += 1

            if p2 - p1 + 1 > k:
                window_count[s2[p1]] -= 1
                if window_count[s2[p1]] == 0:
                    del window_count[s2[p1]]
                p1 += 1
            
            if window_count == target:
                return True
        return False
                # subtract left element
            
            # check if they are equal

        


            