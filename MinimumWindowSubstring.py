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