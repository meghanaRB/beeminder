class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_nums = set(nums)
        leng = len(nums)
        for i in range(0, leng-1):
            diff = target - nums[i]
            if diff in set_nums:
                try:
                    x = nums[i+1:].index(diff)+(i+1)
                    # print(nums[i+1:])
                    return [i, x]
                except:
                    continue
        return []