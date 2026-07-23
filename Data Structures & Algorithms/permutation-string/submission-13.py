class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_1 = Counter(s1)
        freq_2 = Counter()
        k = len(s1)
        p1 = 0
        for p2 in range(len(s2)):
            # first increase size
            freq_2[s2[p2]] += 1

            # then shrink size
            if p2 - p1 + 1 > k:
                freq_2[s2[p1]] -= 1
                if freq_2[s2[p1]] == 0:
                    del freq_2[s2[p1]]
                p1 += 1
            print(p2 - p1 + 1)
            if p2 - p1 + 1 == k: 
                if freq_1 == freq_2:
                    return True
            print(freq_2)

        return False