class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for ch in tokens:

            if ch != "+" and ch != "/" and ch != "-" and ch != "*":
                stack.append(ch)
            else:
                
                right = int(stack.pop())
                left = int(stack.pop())

                if ch == '+':
                    stack.append(left + right)
                elif ch == '-':
                    stack.append(left - right)
                elif ch == '/':
                    #truncate to zero
                    stack.append(left / right)
                elif ch == '*':
                    stack.append(left * right)

        return int(stack.pop())


