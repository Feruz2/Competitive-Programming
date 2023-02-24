class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        for ID, time in logs:
            d[ID].add(time)
        answer = [0]*k
        for i in d.values():
            answer[len(i)-1] += 1
        return answer