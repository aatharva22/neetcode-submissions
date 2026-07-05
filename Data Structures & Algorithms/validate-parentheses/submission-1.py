class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:

            if ch == '{' or ch == '[' or ch =='(':
                stack.append(ch)

            elif ch == '}' or ch == ']' or ch ==')':
                if len(stack) == 0:
                    return False
                if ch == '}':
                    if stack[-1] != '{':
                        return False
                    stack.pop()
                elif ch == ']':
                    if stack[-1] != '[':
                        return False
                    stack.pop()
                elif ch == ')':
                    if stack[-1] != '(':
                        return False
                    stack.pop()
            
        return len(stack) == 0
                
                    
                    

