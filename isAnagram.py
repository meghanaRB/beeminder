from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        if dict_s == dict_t:
            return True
        else:
            return False


##Notes##
        
# - dictionaries can be compared
# - reversed() not reverse()
# - 