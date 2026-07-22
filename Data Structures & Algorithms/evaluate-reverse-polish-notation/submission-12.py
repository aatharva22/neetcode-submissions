class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t == '+' or t == '-' or t=='/' or t == '*':
                op = t
                b = int(stack.pop())
                a = int(stack.pop())
                if op == '+':
                    stack.append(a+b)
                elif op == '-':
                    stack.append(a-b)
                elif op == '/':
                    stack.append(int(a/b))
                elif op == '*':
                    stack.append(a*b)
            else:
                stack.append(int(t))
    
        return stack[-1]