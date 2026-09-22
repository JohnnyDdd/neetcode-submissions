class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        for p in s:
            if p == '(': stack.append(1)
            elif p == '[': stack.append(2)
            elif p == '{': stack.append(3)
            
            elif p == ')' and stack[-1] == 1: stack.pop()
            elif p == ']' and stack[-1] == 2: stack.pop()
            elif p == '}' and stack[-1] == 3: stack.pop()
            else: stack.append(0)
        return (stack == [0])