"""

Author : Shuvam Kumar Singh
Date : 30/01/2024
Problem : 150. Evaluate Reverse Polish Notation
Difficulty : Medium

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for operator in tokens:
            if operator =="+":
                stack.append(stack.pop() + stack.pop())
            elif operator =="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif operator =="*":
                stack.append(stack.pop() * stack.pop())
            elif operator =="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(operator))
        return stack[0]
