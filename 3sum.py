class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums)-2):
            if nums[i]>0:
                continue
            if (i>0 and nums[i]!=nums[i-1]) or (i ==0) :
                start = i+1
                end = len(nums)-1
                while start < end:
                    target = 0-nums[i] 
                    if nums[start] + nums[end] < target:
                        start +=1
                    elif nums[start] + nums[end] > target:
                        end -=1
                    else:
                        res.append([nums[i], nums[start], nums[end]])
                        start+=1
                        end-=1
                        while (nums[start-1]==nums[start]) and start < (len(nums)-2):
                            start+=1
                        while (nums[end+1]==nums[end]) and end > start:
                            end-=1
            
        return res

        
       
# the tricky part is realzing that a single number can have muliple pairs of numbers that all add up to 0
# deduplication done via 'in' operation is a bad idea
#1. same as 2sum but after finding a pair that sums to target, search within the inner loop by moving start and end inwards
#2. from outside, do not repeate the outer loop for two numbers that are the same
#3. from inside, narrow the window (both start and finish) so you skip repeats
        