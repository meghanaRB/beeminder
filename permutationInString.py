from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)< len(s1):
            return False
        
        s1_counter = Counter(s1)
        start = 0
        end = len(s1)-1
        window_counter = Counter(s2[start:end])

        while end < (len(s2)):

            window_counter[s2[end]]+=1
            match_ = s1_counter.get(s2[end], None)
            if match_!=None:
                if window_counter==s1_counter:
                    return True
            window_counter[s2[start]]-=1
            start+=1
            end+=1
        
        return False

## Notee
# the sliding rule is obvious. where you messed up initially is you were creating a new window with every loop instead of removing one char and adding one char