class Solution(object):

    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        operands = {'+', '*', '/', '-'}

        for token in tokens:


            if token in operands:
                
                right_op = stack.pop()
                left_op = stack.pop()
                
                if token == '+':
                    stack.append(left_op + right_op)
                
                elif token == '-':
                    stack.append(left_op - right_op)
                
                elif token == '*':
                    stack.append(left_op * right_op)
                
                elif token == '/':
                    
                    stack.append( int(left_op / right_op) )
                    
            else:

                stack.append(int(token))

            
            
        return stack[-1]
            
## Time Complexity: O(n)
## Space complexity: less than O(n)