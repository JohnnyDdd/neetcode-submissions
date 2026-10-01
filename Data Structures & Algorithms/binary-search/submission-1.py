class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r >= l:
            mid = (r+l) // 2
            mid_num = nums[mid]
            if mid_num == target: return mid
            else:
                if mid_num < target: l = mid + 1
                else: r = mid - 1
        return -1
