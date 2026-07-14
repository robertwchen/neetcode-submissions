class Solution:
    def trap(self, height: List[int]) -> int:
        # Pattern:
        # What algorithm shape is this?
            # prefix sums problem 

        # State:
        # What does each variable/store object mean?
            # max_left = current elements max_height on left side
            # max_right = current elements max_height on the right side
            # current = currnet node

        # Invariant:
        # What must stay true?
            # calculated value must be > 0

        # Progress:
        # What moves/changes every loop or recursive call?

        # Update:
        # When do I count/save/return answer?

        # Return:
        # What type do I return: bool/int/list/node/None?
            # total sum

        # each height is min(max_left, max_right) + current_height
        # calculate max_left and max_right

        # loop through all nodes and calculate sum

        current_max = 0
        left_max = []
        # calculate left_max
        for h in height:
            left_max.append(current_max)
            current_max = max(current_max, h)
        print(left_max)

        current_max = 0
        right_max = []
        for i in range(len(height) - 1, -1, -1):
            right_max.append(current_max)
            current_max = max(current_max, height[i])
        print(right_max)
        right_max.reverse()

        total_area = 0
        for i, h in enumerate(height):
            col_area = min(left_max[i], right_max[i]) - h
            total_area += max(0, col_area)
            print(i, col_area)

        return total_area


                