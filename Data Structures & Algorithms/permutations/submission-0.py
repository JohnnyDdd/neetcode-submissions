class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        results = []
        n_set = set(nums)
        def backtrack(cur, items):
            if len(cur) == len(nums):
                results.append(list(cur))
                return
            for item in items:
                sub_items = items.copy()
                sub_items.remove(item)
                cur.append(item)
                backtrack(cur, sub_items)
                cur.pop()
        backtrack([], n_set)
        return results