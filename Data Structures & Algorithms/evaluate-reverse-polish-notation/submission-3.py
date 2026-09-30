class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        ops = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b, 
            "/": lambda a, b: int(a / b)
            }


        for token in tokens:
            if token not in ops:
                num.append(int(token))
            else:
                num1 = num.pop()
                num2 = num.pop()
                num.append(ops[token](num2, num1))
        
        return num[0]
