from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        k = len(t)
        if len(s)<k:
            return ""
        
        min_window = ""
        
        t_counts = Counter(t)
        window_counts = Counter()

        end = 0
        start = 0
        matches = 0

        min_window=""

        for end in range(len(s)):

            window_counts[s[end]]+=1

            if window_counts[s[end]]==t_counts[s[end]]:
                matches+=1

            while matches>=len(t_counts):
                if (len(s[start:end+1]) < len(min_window)) or min_window == "" :
                    min_window = s[start:end+1]
 
                if s[start] in t_counts:
                    window_counts[s[start]]-=1

                    if window_counts[s[start]]<t_counts[s[start]]:
                        matches-=1

                
                start+=1

        return min_window
    
# ####notes
# Pattern. Variable-size sliding window, "shortest valid" flavor.
# Core idea. Grow the right pointer until the window first contains all required characters. Then shrink from the left as far as you can while still being valid. Record the window size at each valid state. When shrinking breaks validity, resume growing.
# The key trick: the matches integer.
# Maintain a count of how many distinct characters in t currently have their full required count met by the window. The window is valid exactly when matches == len(t_counts) — a single integer comparison, not a scan over the alphabet.
# matches updates incrementally:

# On adding a character c: if c is in t and window_counts[c] just hit t_counts[c], increment matches.
# On removing a character c: check before decrementing — if window_counts[c] is currently equal to t_counts[c], removing it will break the requirement, so decrement matches.

# Asymmetric checks (after-increment going up, before-decrement going down) catch the exact crossing of the requirement line.