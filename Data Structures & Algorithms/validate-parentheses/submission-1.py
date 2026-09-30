class Solution:
    def isValid(self, s: str) -> bool:
        valid = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                valid.append(char)
            else:
                check = valid[-1] if valid else False
                if (check == '(' and char == ')') or (check == '[' and char == ']') or (check == '{' and char == '}'):
                    valid.pop()
                else:
                    return False
        
        if not valid:
            return True

        return False