class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == "../" and stack:
                stack.pop()
            elif logs[i] != "./" and logs[i] != "../":
                stack.append(logs[i])
        return len(stack)
                
        