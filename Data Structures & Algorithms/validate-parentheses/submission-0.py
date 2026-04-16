class Solution:
    def isValid(self, s: str) -> bool:
        chars = {")" : "(", "}" : "{", "]" : "["}        
        stack = ["a"]

        for char in s:
            if char in chars:
                if chars[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return stack[-1] == stack[0]