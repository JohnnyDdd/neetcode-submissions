class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        final = False
        def backtracking(y,x,i,visited):
            res = False
            letter = word[i]
            cur = board[y][x]
            if letter == cur:
                if i == len(word)-1:
                    return True
                
                l,r,d,u = x > 0, x < len(board[0]) - 1, y > 0, y < len(board) - 1

                if l and (y,x-1) not in visited:
                    visited.append((y,x-1)) 
                    res = res or backtracking (y, x-1, i+1, visited)
                    visited.pop()
                if r and (y,x+1) not in visited: 
                    visited.append((y,x+1))
                    res = res or backtracking (y, x+1, i+1, visited)
                    visited.pop()
                if d and (y-1,x) not in visited: 
                    visited.append((y-1,x))
                    res = res or backtracking (y-1, x, i+1, visited)
                    visited.pop()
                if u and (y+1,x) not in visited:
                    visited.append((y+1,x)) 
                    res = res or backtracking (y+1, x, i+1, visited)
                    visited.pop()
                return res
            else: return False
        for x in range(len(board[0])):
            for y in range(len(board)):
                if board[y][x] == word[0]: 
                    final = final or backtracking(y,x,0,[(y,x)])
        return final