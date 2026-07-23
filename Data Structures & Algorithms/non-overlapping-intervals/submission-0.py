# where am I
    # at some point on the array
# what am I doing
    # check if there is overlap by end
# what do I return
    # number of removals

# [4, 5] [2, 6] [6,10]
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_by_end = sorted(intervals,key = lambda interval:interval[1])
        print(sorted_by_end)
        
        count = 0
        i = 0
        for i in range(0, len(sorted_by_end) - 1):
            if sorted_by_end[i + 1][0] < sorted_by_end[i][1]: #overlap found
                count += 1
                sorted_by_end[i + 1] = sorted_by_end[i]
        return count
