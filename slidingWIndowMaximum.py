class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        outputs = []
        for i in range(len(nums)-k+1):

            # print(nums[i:i+k])
            x = max(nums[i:i+k])

            outputs.append(x)


        # print(outputs)
        return outputs


##brute force -- nexts to be modified



