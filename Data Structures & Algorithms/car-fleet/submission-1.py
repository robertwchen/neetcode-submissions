class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Goal: Return different groups of cars, find where cars intersect at distance 10
            # goal: find convergences before distance 10
        # Store: set of positions of each car at each time and check if same: 
        # Valid:
        # Fix:
        # Answer:

        cars = []
        sorted_cars = []
        # so first store pos, speed array
        for i, p in enumerate(position):
            s = speed[i]
            cars.append((p, s))
        sorted_cars = sorted(cars, key = lambda car:car[0], reverse=True)

        # now use stack to count fleets if time to target > last element pop element
        stack = []
        for p, s in sorted_cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            


        