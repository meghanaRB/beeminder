class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a = set()
        for number in nums:
            if number not in set_a:
                set_a.add(number)
            else:
                return True
        return False