class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod= []
        preprod.append(1)
        
        prod = 1
        for i in range(1, len(nums)):
            prev= nums[i-1]
            prod = prev * prod
            preprod.append(prod) 
           
        prod = 1
        
        i=len(nums) - 2
        while i>=0:
            next_ = nums[i+1]
            prod = next_ * prod
            preprod[i] = prod * preprod[i]
            i-=1

        return preprod

       # time complexity : O(n)
       # space complexity : O(n) 