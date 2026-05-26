class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/' and tokens[i] != '*':
                stack.append(int(tokens[i]))
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(op1 + op2)
                elif tokens[i] == '-':
                    stack.append(op1 - op2)
                elif tokens[i] == '/':
                    stack.append(int(op1 / op2))
                elif tokens[i] == '*':
                    stack.append(op1 * op2)
            
        return stack.pop()

                    