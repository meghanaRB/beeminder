class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix[0])
        lo, hi = 0, len(matrix)*n - 1

        while lo <= hi:

            mid = lo + (hi - lo)//2

            col = mid%n
            row = mid//n

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


        
        