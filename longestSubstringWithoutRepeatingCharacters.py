class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        
        start = 0
        end = 0
        max_sub = 0
        position_of_chars = {}
        # ?\position_of_chars[s[end]]=0
        while end < len(s):
            key = position_of_chars.get(s[end], None)

            if key!=None and (key>=start):
                start = position_of_chars[s[end]]+1
            
            position_of_chars[s[end]] = end
            end+=1
                       
            max_sub=max(max_sub, end - start)   
         
        return max_sub

# Time Complexity: O(n)
# Space Complexity: O(1)

#Solution: Sliding Window
# Window expands with every iteration of the for-loop while the hash keeps works as a lookup for arriving at the start of the window
#if you come across a letter already in the window, then the window needs to start from the next char after the previous occurance of the letter you found
#where I tripped: remember that the new start can only be after the old start -- a sliding window start should never go back
#the hashmap exists to only find the next position of the start. no need to delete older windows from it