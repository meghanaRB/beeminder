class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        valid_parenthesis = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        
        for char in s:

            if char not in valid_parenthesis:
                stack.append(char)
            
            else:

                if len(stack)==0:
                    return False

                if valid_parenthesis.get(char)!=stack[-1]:
                    return False

                else:
                    stack.pop()
            

        return len(stack)==0 
    
    ##easy, no notes