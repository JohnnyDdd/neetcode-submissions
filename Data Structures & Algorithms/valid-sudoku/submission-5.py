class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sub = defaultdict(set)

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == '.': continue
                if item in row[i]: return False
                if item in col[j]: return False
                if item in sub[(i//3,j//3)]: return False

                else:
                    row[i].add(item)
                    col[j].add(item)
                    sub[(i//3,j//3)].add(item)
        return True