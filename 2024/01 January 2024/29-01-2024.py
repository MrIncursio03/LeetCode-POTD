"""

Author : Shuvam Kumar Singh
Date : 27/01/2024
Problem : 232. Implement Queue using Stacks
Difficulty : Easy

"""


class MyQueue:

    def __init__(self):
        self.l=[]

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        if self.l:
            return self.l.pop(0)

    def peek(self) -> int:
        if self.l:
            return self.l[0]

    def empty(self) -> bool:
        if self.l:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
