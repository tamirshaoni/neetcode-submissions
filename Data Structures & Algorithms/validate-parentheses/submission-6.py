class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 :
            return False

        parentheses = {')' : '(', ']' :'[', '}' : '{'}
        stack = []

        for c in s:
            if c in parentheses and stack:
                if parentheses[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else: 
            return False
            
