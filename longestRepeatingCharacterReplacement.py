from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        max_freq = 0
        longest = 0
        start = 0
        
        for end in range(len(s)):
            # grow: add s[end] to window
            counts[s[end]]+=1
            # update max_freq (only ever grows)
            max_freq = max(max_freq, counts[s[end]])
            # shrink: while window invalid, remove s[start], advance start

            len_sub = end - start + 1

            if (len_sub - max_freq) > k:
                counts[s[start]]-=1
                start+=1

            longest = max(longest, end - start + 1)

            # record longest
        
        return longest
    
## Notes
## 1. we update the the counter counts with every iteration with the end. the end is monotonically increasing like most sliding window problems
##2. we need to figure out if our substring's length minus the most frequently orrcuring elements is less than k -- in which case, we can increase the window. If not, the winow is invalid and we move start
##3. the trick is in maintianing a stale freq. even though counts decrements start char at every sreset, the max_freq is a memory of the largest "team" we have ever seen
##4. max_freq might not show you the maximum frequecy in the current substring. but we don't need that. If the current substring is the longest, then it will grow eventually
