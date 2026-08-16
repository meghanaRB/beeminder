class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums)-1

        while lo <  hi:

            mid = (hi + lo) // 2

            if nums[mid] < nums[hi]:

                hi = mid 
            
            else:

                lo = mid + 1 
        
        return nums[lo]




#### Notes ####
## Time Complexity : O(log n)
## Space Complexity : 1
## do you need several compares for this? to know where lowest element is, you need to compare only mid and hi
## the most imporant place where you trip is in choosing the mid update. do you discard? do you keep?

