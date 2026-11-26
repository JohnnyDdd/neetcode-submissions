class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        def is_pal(s):
            if not s or len(s) == 1: return True
            if s[0] == s[-1]: return is_pal(s[1:-1])
            return False
        def backtracking(cur, i):
            
            if i == len(s):
                results.append(list(cur))
                return

            for j in range(i+1, len(s)+1):
                if is_pal(s[i:j]):
                    cur.append(s[i:j])
                    backtracking(cur, j)
                    cur.pop()
        backtracking([],0)
        return results

