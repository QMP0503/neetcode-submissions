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
            if token not in ops: #isdigit() will fail with "-11"
                num.append(int(token))
            else:
                b, a = num.pop(), num.pop()
                num.append(ops[token](a, b))
        
        return num[0]
