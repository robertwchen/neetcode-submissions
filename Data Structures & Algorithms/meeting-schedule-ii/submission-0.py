"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()
        p1 = 0
        p2 = 0
        max_count = 0
        count = 0
        while p1 < len(intervals):
            print(count, start[p1], end[p2])
            if start[p1] == end[p2]:
                p1 += 1
                p2 += 1

            elif start[p1] < end[p2]:
                count += 1
                p1 += 1

            elif start[p1] > end[p2]:
                p2 += 1
                count -= 1
            max_count = max(max_count, count)
        return max_count
           



        
        # ok so basically look for overlaps and pop them off to a new list 