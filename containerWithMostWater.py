class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_area = 0

        while p2 > p1:
            max_area = max(max_area, min(height[p1], height[p2])*(p2-p1)  )
           
            if (p2-p1)==1:
                break
            
            if height[p1] <  height[p2]:
                next_p1 = p1
                while (next_p1 <= p2):
                    if height[next_p1+1] > height[next_p1]:
                        p1 = next_p1+1
                        break
                    else:
                        next_p1+=1
                    # break
            else:
                next_p2 = p2
                while (next_p2 >= p1):
                    if height[next_p2-1] > height[next_p2]:
                        p2 = next_p2-1
                        break
                    else:
                        next_p2-=1
        
        return max_area
            
########################################
## - two pointers always involve finding maxing or minimum or a measure
## -  the approach will always lie along the path of moving the pointers and when to move them
## - remember, when searching for max, you do not need to keep the pointer indices of the max in memory
        

                    



                  


        