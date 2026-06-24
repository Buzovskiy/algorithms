from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                if len(stack):
                    stack.pop()
            elif op == "D":
                if len(stack):
                    stack.append(stack[-1]*2)
            elif op == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                num = int(op)
                stack.append(num)
            print(stack)
        if len(stack):
            return sum(stack)
        else:
            return 0
