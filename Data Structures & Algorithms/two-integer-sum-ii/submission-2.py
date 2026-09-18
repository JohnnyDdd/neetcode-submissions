class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            ni = numbers[i]
            nj = numbers[j]
            if ni + nj == target: return [i+1,j+1]
            if ni + nj > target: j -= 1
            else: i += 1 