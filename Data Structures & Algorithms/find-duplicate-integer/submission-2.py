class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x, y = 0, 0
        while True:
            x, y = nums[x], nums[nums[y]]
            if x == y: break
        x = 0
        while True:
            x, y = nums[x], nums[y]
            if x == y: break
        return x
