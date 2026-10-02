class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            print(nums[l],nums[mid])
            if nums[mid] == target: return mid
            
            if nums[mid] >= nums[r]:
                if target <= nums[mid] and nums[l] <= target: r = mid-1
                else: l = mid+1
            
            else:
                if nums[mid] <= target and nums[r] >= target: l = mid+1
                else: r = mid-1

        return -1