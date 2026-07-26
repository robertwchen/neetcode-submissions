

# where am I 
    # at some substring on the array
# what am I doing
    # check have vs have not
# what do I reutrn
    # shortest possible substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = float('inf')
        shortest_left = 0
        shortest_right = 0
        freq_t = Counter(t)
        freq_s = Counter()
        have = 0
        need = len(freq_t)

        left = 0

        for right in range(len(s)):
            # increase current size
            c = s[right]
            freq_s[c] += 1

            if freq_t[c] == freq_s[c]:
                have += 1
            
            while have == need:
                c = s[left]
                print(have, need, c)
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    shortest_left, shortest_right = left, right

                freq_s[c] -= 1
                left += 1

                if freq_t[c] > freq_s[c]:
                    have -= 1
        return s[shortest_left: shortest_right + 1] if shortest != float('inf') else ""

                # try remove

            

            # check conditions
