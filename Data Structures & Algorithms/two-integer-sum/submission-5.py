class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {nums[x]: x for x in range(len(nums))}
        for i in range(len(nums)):
            diff_i = target - nums[i]
            if diff_i in dict and dict[diff_i] != i:
                return [i, dict[diff_i]]
        return []