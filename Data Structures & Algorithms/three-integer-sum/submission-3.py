class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Pattern:
        # What algorithm shape is this?
            # sorting then 2 pointer for each value in the array

        # State:
        # What does each variable/store object mean?
            # the current num means num looking for 2 nums for
            # p1 is the element just right of current
            # p2 is element at end

        # Invariant:
        # What must stay true?
            # list sorted, p1 < p2 can't double count
            # distinct triplets


        # Progress:
        # What moves/changes every loop or recursive call?
            # current moves forward, p1 p2 work inwards

        # Update:
        # When do I count/save/return answer?
            # when the current moves to end

        # Return:
        # What type do I return: bool/int/list/node/None?
            # return list of lists


        # initialize list []
        triplets = []
        nums.sort()

        # loop through all elements up to second to last elements
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            # initialize the two pointers (must be inbounds)
            # if num is the same as last num considered 
                # continue
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if (p1 > i + 1) and (nums[p1] == nums[p1 - 1]):
                    p1 += 1
                    continue
                if (p2 + 1 < len(nums)) and nums[p2] == nums[p2 + 1]:
                    p2 -= 1
                    continue

                if sum == 0:
                    triplets.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                elif sum > 0:
                    p2 -= 1
                # if find match add to list

                # if < target move up p1 
                # if > target move p2 down
        return triplets
