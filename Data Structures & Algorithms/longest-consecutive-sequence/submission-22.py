class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lens = [0]
        set_num = set(nums)
        for num in set_num:
            if num - 1 not in set_num:
                len_n = 1
                pivot = num
                while pivot + 1 in set_num:
                    len_n += 1
                    pivot += 1
                lens.append(len_n)
        return max(lens)


