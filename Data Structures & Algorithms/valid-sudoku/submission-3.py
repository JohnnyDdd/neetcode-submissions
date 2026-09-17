class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for rows
        for row in board:
            appr = {}
            for n in row:
                if n == '.': continue 
                if n not in appr.keys(): appr[n] = 1
                else: return False

        transpose = [list(row) for row in zip(*board)]
        # check for cols
        for col in transpose:
            appr = {}
            for n in col:
                if n == '.': continue
                if n not in appr.keys(): appr[n] = 1
                else: return False

        # check for sub squares
        for i in range(0,7,3):
            for j in range(0,7,3):
                appr = {f'{x}':1 for x in range(1,10)}
                sub = [item for row in ([board[0+i][j:3+j],board[1+i][j:3+j],board[2+i][j:3+j]]) for item in row]
                print(sub)
                for item in sub: 
                    if item == '.': continue
                    if item in appr.keys():
                        if appr[item] != 1: return False
                        else: appr[item] = 0
        return True