class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        countedNums=Counter(nums)
        for n in nums:
            if n not in dict_nums.keys(): dict_nums[n] = 1
            else: dict_nums[n] += 1
        #print(countedNums)
        #newList = list(reversed(list(set(countedNums))))
        newList = list(set(countedNums.most_common(k)))
        return [x[0] for x in newList]