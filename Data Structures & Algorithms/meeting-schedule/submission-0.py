"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# where am I

# what am I doing
# what do I return

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda interval:interval.start)
        i = 0
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i + 1].start < sorted_intervals[i].end:
                return False
        return True
