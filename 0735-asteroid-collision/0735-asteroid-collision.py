class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
                i += 1
            elif (stack[-1] * asteroids[i]) >= 1:
                stack.append(asteroids[i])
                i += 1
            elif stack[-1] < 0 and asteroids[i] > 0:
                stack.append(asteroids[i])
                i += 1
            elif stack[-1] == abs(asteroids[i]):
                stack.pop()
                i += 1
            elif stack[-1] < abs(asteroids[i]):
                stack.pop()
            else:
                i += 1
            # print(stack)
        return stack