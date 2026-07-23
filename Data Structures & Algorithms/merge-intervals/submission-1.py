class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval:interval[0])

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= results[-1][1]:
                updated_start = min(intervals[i][0], results[-1][0])
                updated_end = max(intervals[i][1], results[-1][1])
                results[-1] = [updated_start, updated_end]
            else:
                results.append(intervals[i])
            i += 1
        return results