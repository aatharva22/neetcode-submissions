class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):

            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(s[i])
            
            elif s[i] == '}' or s[i] == ']' or s[i] == ')':

                if len(stack) == 0:
                    return False
                else:
                    match stack[-1]:
                        case '{':
                            if s[i] == '}':
                                stack.pop() 
                            else:
                                return False
                        case '[':
                            if s[i] == ']':
                                stack.pop()
                            else:
                                return False 
                        case '(':
                            if s[i] == ')':
                                stack.pop() 
                            else:
                                return False
        
        if len(stack) == 0:
            return True
        else:
            return False




        