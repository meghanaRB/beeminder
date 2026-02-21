class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        for i in t:
            if t.count(i)==s.count(i):
                continue
            else:
                return False

        return True
            
