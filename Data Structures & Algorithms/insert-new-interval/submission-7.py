class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)

        # skip end before current starts
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)
        result.extend(intervals[i:])

        return result