class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []
        ret = []
        #print(f"{nums[-1]} - bef: {nums}")
        cur = nums.pop()
        i = 1
        
        while i*cur < target:
            dum_nums = nums.copy()
            sub_target = target - i*cur
            sub_combs = self.combinationSum(dum_nums, sub_target)
            if sub_combs:
                for comb in sub_combs:
                    ret.append(comb + i*[cur])
            i += 1
        
        if i*cur == target:
            ret.append(i*[cur])
        #print(f"{cur} - aft: {nums}")
        return ret + self.combinationSum(nums,target)