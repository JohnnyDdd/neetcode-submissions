class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        def backtracking(start,cur):
            results.append(list(cur))
            for i in range (start, len(nums)):
                item = nums[i]
                if i != start and item == nums[i-1]: continue

                cur.append(item)
                backtracking(i+1, cur)
                cur.pop()

        backtracking(0,[])
        return results