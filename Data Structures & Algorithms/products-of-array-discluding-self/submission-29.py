class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #single left to right run, where each element is contaisn the product of all before it
        #single right to left run, where each element contains the product of all before it
        #the 2nd run multiplies with the list from the fist run, return that list
        n = len(nums)
        fRun = [1,nums[0]]
        for i in range(2,n):
            factor = fRun[-1]
            fRun.append(nums[i-1] * factor)
        sRun = [1,nums[n-1]]
        for j in range(n-2,0,-1):
            factor = sRun[-1]
            sRun.append(nums[j] * factor)
        sRun.reverse()

        return [ n*m for n,m in zip(fRun,sRun)]




