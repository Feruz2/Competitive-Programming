class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        x_string = 'ab'
        y_string = 'ba'

        if x < y:
            x,y = y,x
            x_string,y_string = y_string,x_string

        stack = []
        points = 0

        for i in range(len(s)):
            if stack and stack[-1] + s[i] == x_string:
                stack.pop()
                points += x
                continue

            stack.append(s[i])

        stack2 = []
        for i in range(len(stack)):
            if stack2 and stack2[-1] + stack[i] == y_string:
                stack2.pop()
                points += y
                continue

            stack2.append(stack[i])

        return points