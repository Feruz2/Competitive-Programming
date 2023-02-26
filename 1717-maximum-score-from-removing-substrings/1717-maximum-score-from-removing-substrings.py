class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        points = 0

        if x > y:
            remove_first = "ab"
            remove_next = "ba"
        else:
            remove_first = "ba"
            remove_next = "ab"

        # The first Iteration
        for char in s:
            stack.append(char)

            if len(stack) > 1 and stack[-2] + stack[-1] == remove_first:
                stack.pop()
                stack.pop()

                points += max(x, y)

        # The second Iteration
        stack2 = []
        for char in stack:
            stack2.append(char)

            if len(stack2) > 1 and stack2[-2] + stack2[-1] == remove_next:
                stack2.pop()
                stack2.pop()

                points += min(x, y)

        return points