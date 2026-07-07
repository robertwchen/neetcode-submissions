class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c_count = Counter()

        # first start with window 0, 0, slide p2 up every time
        p1 = 0
        max_len = 0
        for p2 in range(0, len(s)):
            # add c to counter
            c_count[s[p2]] += 1
            
            max_freq = 0
            max_freq_c = s[p2]
            # max freq = 0 
            # max_freq_c = None
            for c in c_count:
                if c_count[c] > max_freq:
                    max_freq_c = c
                    max_freq = c_count[c]

            window_size = p2 - p1 + 1
            while window_size - max_freq > k:
                c_count[s[p1]] -= 1
                p1 += 1
                window_size = p2 - p1 + 1

            max_len = max(max_len, window_size)
            print(p1, p2, max_len)
        return max_len

            # while window size minus max-freq > k:
                # remove p1 char
                # p1 += 1
            

            

