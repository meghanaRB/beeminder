class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        is_preset  = set(nums)
        chain = 0
        for n in is_preset:
            if n-1 not in is_preset:
                next_ = n + 1
                seq=1
                while next_ in is_preset:
                    next_ = next_ + 1
                    seq+=1
                
                chain = max(chain, seq)
            
        return chain

# the inner loop

                

        