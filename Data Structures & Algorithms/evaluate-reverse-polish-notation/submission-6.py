class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for a in tokens:
            try:
                int(a)
                stack.append(int(a))
            except ValueError:
                if a == '+':
                    y, x = stack.pop(), stack.pop()
                    stack.append(x+y)
                elif a == '-':
                    y, x = stack.pop(), stack.pop()
                    stack.append(x-y)
                elif a == '*':
                    y, x = stack.pop(), stack.pop()
                    stack.append(x*y)
                elif a == '/':
                    y, x = stack.pop(), stack.pop()
                    stack.append(int(x/y))
        return stack.pop()