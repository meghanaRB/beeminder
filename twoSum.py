class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_indices = {}
        for i in range(0, len(nums)):
            dict_indices[target - nums[i]]=i
        
        for i in range(0, len(nums)):
            key_ = dict_indices.get(nums[i])
            if key_ and (i!=key_):
                return [i, dict_indices.get(nums[i])]

        

        # print(nums)

        # while start<=end:
        #     print("start num: ", nums[start])
        #     print("end num: ", nums[end])
        #     print("start: ", start)
        #     print("end: ", end)
        #     if (nums[end] + nums[start]) > target:
        #         print("here")
        #         end =-1
        #     elif (nums[end] + nums[start]) < target:
        #         start+=1
        #     else:
        #         return [dict_indices[nums[start]], dict_indices[nums[end]]]










        

