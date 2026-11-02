class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        cur = nums.pop()
        #print(cur)
        ret = []
        sub_subset = self.subsets(nums)
        for subset in sub_subset:
            ret.append(subset + [cur])
        #print(ret)
        return (ret + sub_subset)
