class MinStack(object):
    
    # list_of_elements = []
    # min_elements = None

    def __init__(self):

        self.list_of_elements = []
        self.min_elements = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        self.list_of_elements.append(val)

        if not self.min_elements:
            self.min_elements.append(val)
        
        else:
            
            self.min_elements.append(min(self.min_elements[-1], val))
            

    def pop(self):
        """
        :rtype: None
        """
       
        if self.list_of_elements:

            self.min_elements.pop()
            return self.list_of_elements.pop()

      
    def top(self):
        """
        :rtype: int
        """
        if self.list_of_elements:
            return self.list_of_elements[-1]
        return None
        

    def getMin(self):
        """
        :rtype: int
        """

        if self.min_elements:
            return self.min_elements[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




##Notes:

# Time Complexity: O(1)

# Space Complexity: O(n)


# Where I got stuck:
# Trying to keep min_elements sorted is not the right approach. That cannot be accomplished in O(1). My instinct was inswertsort
# Remember, min_elements is only a track of the minumum element at each point of the stock. It contains duplicate information as is necessary