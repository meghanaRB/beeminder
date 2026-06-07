class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position, speed = zip(*sorted(zip(position, speed), reverse = True))

        stack = []

        for i in range(len(position)):

            t_arrival = (target - position[i])/speed[i]
            
            if stack:
                if stack[-1]<t_arrival:
                    stack.append(t_arrival)

            else:
                stack.append(t_arrival)
            
        return len(stack)

##Notes:

# Time Complexity: O(n log n) from sort
# Space Complexity: O(n)

#Trick:
# We need to start looking at cars from the closest to the target. The one immediately behind it can join it for form a fleet, or it is too slow to do so. Remember, cars can't pass each other
# the time of arrival is the metric to track
# For two cars A and B, let A be ahead of car B
# A arrives at t_a and b arrives at t_b,
# If t_b < t_a, then B can catch up to A and they form a fleet
#if not, add B to the stack and repeat for the next car
