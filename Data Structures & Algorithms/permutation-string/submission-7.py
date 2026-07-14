class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# Return:
# What exactly am I returning?
    # boolean of true or false if substring of s2 in s1

# Example:
# Tiny input + expected output by hand
    # s1 abc, s2 lecabee -> true cab

# Brute:
# Dumb obvious way, even if slow
    # look through every elngth recalculate every length to see if it is permutation

# Property:
# What special clue can improve brute force?
# sorted? BST? contiguous? frequency? top k? level order?
    # sliding window fixed size

# Pattern:
# sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
    # sliding window

# State:
# What variables/data structures do I need?
    # set of all current chars in the window

# Invariant:
# What must stay true?
    # window must contain only elements in the set

# Progress:
# What moves/changes each step?

# Update:
# When do I count/save/return answer?

        p1 = 0
        p2 = len(s1)
        freq_s1 = Counter(s1)# first turn s1 into a freq counter: 
        freq_s2 = Counter(s2[0:p2]) # take first len(s2) into a freq counter

        while p2 < len(s2):
            if freq_s1 == freq_s2:
                return True

            c1 = s2[p1]
            c2 = s2[p2]

            freq_s2[c2] = 1 + freq_s2.get(c2, 0)
            freq_s2[c1] -= 1
            if freq_s2[c1] == 0:
                del freq_s2[c1]
            p1 += 1
            p2 += 1 
            print(freq_s1)
            print(freq_s2)
            
        return freq_s1 == freq_s2