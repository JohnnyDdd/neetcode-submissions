class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0]*n
        stack = []
        for i in range(n):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]:
                ret[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return ret