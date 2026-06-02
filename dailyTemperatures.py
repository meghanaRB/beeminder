class Solution: 

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        outputs = [0 for i in range(len(temperatures))]

        if len(temperatures)==1:
            return outputs

        stack.append(0)

        for i in range(1, len(temperatures)):

            while len(stack)>0 and (temperatures[i] > temperatures[stack[-1]]):
                
                next_day = i - stack[-1]
                outputs[stack[-1]] = next_day
                stack.pop()
            
            stack.append(i)
        
        return outputs
    

## Notes
# Time Complexity: O(n)
# Space Complexity: O(n)
# The recognition cue for the pattern: "For each element, find the next/previous greater/smaller element." Any variation of that sentence → monotonic stack.
# Monotonic stack: a stack that maintains a sorted invariant — either strictly increasing or strictly decreasing from bottom to top — by evicting elements that would violate the order before pushing a new one.
# (An invariant is a property that stays true at every step of an algorithm. It's a guarantee you make and then maintain.)