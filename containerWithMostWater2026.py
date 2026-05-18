class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lp = 0
        rp = len(height) - 1 
        max_area = 0

        while lp<rp:
            ##check area with current right and left 
            h = min(height[lp], height[rp])
            l = rp - lp 
            curr_area = h * l
            
            ##left?
            if height[lp] < height[rp]:
                lp+=1
            else:
                rp-=1

            max_area = max(max_area, curr_area)

        return max_area

            

             
# we only need to move if moving help. so question is, which direction?
# area can increase only either of the lengths increases. we start at opposite ends (to maximise length)
# Termination: width strictly decreases by 1 each step.
# Time/space: O(n), O(1).


          







        