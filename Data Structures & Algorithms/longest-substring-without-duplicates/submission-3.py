class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # Return:
    # What exactly am I returning?
        # longest substring no repeat

    # Example:
    # Tiny input + expected output by hand
        # input = "xyzx" output = 3

    # Brute:
    # Dumb obvious way, even if slow
        # every possible substring combinatation so find every substring o(n^2)

    # Property:
    # What special clue can improve brute force?
    # sorted? BST? contiguous? frequency? top k? level order?
        # we can check current substring 

    # Pattern:
    # sliding window / stack / heap / binary search / DFS / BFS / DP / etc.
        # sliding window with set of current c in substring

    # State:
    # What variables/data structures do I need?
        # c_set, p1, p2, longest_length

    # Invariant:
    # What must stay true?
        # substring must only contain unique chars

    # Progress:
    # What moves/changes each step?
        # if p2 in char:
            # remove 1
        # if p2 not in char: then move up and capture 

    # Update:
    # When do I count/save/return answer?
        # return once p2 hits end 

        c_set = set()
        p1 = 0
        p2 = 0
        max_length = 0

        while p2 < len(s):
            while s[p2] in c_set:
                c_set.remove(s[p1])
                p1 += 1
            c_set.add(s[p2])
            current_length = p2 - p1 + 1
            max_length = max(current_length, max_length)
            p2 += 1


        return max_length
