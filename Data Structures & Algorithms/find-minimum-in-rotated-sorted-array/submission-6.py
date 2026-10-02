class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = 0
        while l <= r:
            mid = (l+r)//2
            #print(l,r,mid)
            if nums[mid] < nums[mid-1]: return nums[mid]
            else:
                if nums[r] > nums[mid]: r = mid
                else: l = mid + 1
        return nums[mid]
        

