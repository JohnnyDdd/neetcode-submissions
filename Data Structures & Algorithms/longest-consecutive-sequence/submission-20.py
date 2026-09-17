class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        len_candidates = {num: 1 for num in nums}
        set_num = set(nums)
        for num in set_num:
            if num - 1 not in set_num:
                pivot = num
                while pivot + 1 in set_num:
                    for x in set_num:
                        if x == pivot + 1: 
                            len_candidates[num] += 1
                            pivot = x
        return max(len_cand for len_cand in len_candidates.values())


