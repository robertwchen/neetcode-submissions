class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_list = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            self.two_pointer_sequence(solution_list, sorted_nums, i)

        return solution_list
            

    def two_pointer_sequence(self, solution_list, sorted_nums, i):
        p1 = i + 1
        p2 = len(sorted_nums) - 1

        while p1 < p2:
            total = sorted_nums[i] + sorted_nums[p1] + sorted_nums[p2]

            if total == 0:
                solution_list.append([sorted_nums[i], sorted_nums[p1], sorted_nums[p2]])

                p1 += 1
                p2 -= 1

                while p1 < p2 and sorted_nums[p1] == sorted_nums[p1 - 1]:
                    p1 += 1

                while p1 < p2 and sorted_nums[p2] == sorted_nums[p2 + 1]:
                    p2 -= 1

            elif total < 0:
                p1 += 1

            else:
                p2 -= 1

#sol = Solution()
#nums = [-1,0,1,2,-1,-4]
#sorted_nums = sorted(nums)

#print(sorted_nums)
#print(sol.two_pointer_sequence(sorted_nums, 0))
#print(sol.two_pointer_sequence(sorted_nums, 1))



# output is return state, (found, p1,p2,)