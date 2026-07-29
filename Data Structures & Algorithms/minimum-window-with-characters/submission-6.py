# where am I
    # some subarray
# what am I doing
    # if valid keep shrinking till invalid
# what do I return

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = Counter(t)
        current_window = Counter()

        min_p1 = 0
        min_p2 = 0
        min_size = float('inf')

        need = len(target)
        have = 0

        p1 = 0
        for p2 in range(len(s)):
            if s[p2] in target:
                current_window[s[p2]] += 1

            if s[p2] in target and current_window[s[p2]] == target[s[p2]]:
                have += 1

            while have == need:
                print(p1, p2)
                if p2 - p1 + 1 < min_size:
                    min_size =  p2 - p1 + 1
                    min_p1 = p1
                    min_p2 = p2
                # shrink by 1
                first_char = s[p1]
                if first_char in target:
                    current_window[first_char] -= 1
                    if current_window[first_char] < target[first_char]:
                        have -= 1
                p1 += 1

        return s[min_p1:min_p2 + 1] if min_size != float('inf') else ""
        