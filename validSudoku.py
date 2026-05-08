from collections import defaultdict
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        grid_dict = defaultdict(set)

        def get_grid(i, j):
            return (3*(i//3) + (j//3) + 1)

            
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row_dict[i]:
                    return False
                else:
                    row_dict[i].add(board[i][j])

                if board[i][j] in col_dict[j]:
                    return False
                else:
                    col_dict[j].add(board[i][j])

                if board[i][j] in grid_dict[get_grid(i, j)]:
                    return False
                else:
                    grid_dict[get_grid(i, j)].add(board[i][j])
        return True