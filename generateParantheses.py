class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        num_close = num_open = 0
        outputs = []
        stack = []

        def recursive_gen(stack, num_close, num_open):
            if (num_close == n) and (num_open == n):
                outputs.append(''.join(stack))
            
            
            if num_open < n:
                    stack.append("(")
                    recursive_gen(stack, num_close, num_open+1)
                    stack.pop()

            if num_close < num_open:
                    stack.append(")")
                    recursive_gen(stack, num_close+1, num_open)
                    stack.pop()

            

            # print(stack)

            
        recursive_gen(stack, num_close, num_open)

        return outputs

    
##Notes:
# Time Complexity: 4^n (upper bound)
#Space Complexity: O(n)
##REDO