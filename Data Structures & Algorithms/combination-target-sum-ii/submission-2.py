class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        candidates.sort()
        results = []
        def backtrack(cur, index, cur_sum):
            if cur_sum > target: return
            if cur_sum == target: results.append(list(cur))
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: continue   
                c = candidates[i]
                cur.append(c)
                backtrack(cur, i+1, cur_sum + c)
                cur.pop()
        backtrack([],0,0)
        return results
