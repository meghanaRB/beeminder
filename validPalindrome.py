class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            
            while (s[lp]==' ' or s[lp].isalnum()==False)  and lp < rp:
                lp+=1
            while (s[rp]==' ' or s[rp].isalnum()==False) and rp > lp:
                rp-=1

            if s[lp].lower()!=s[rp].lower():
                print(s[lp].lower(), s[rp].lower())
                return False
            lp+=1
            rp-=1
        
        return True