class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            if len(stack) == 0 or temperatures[i] < stack[-1][0]:
                stack.append([temperatures[i],i])
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    result[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([temperatures[i],i])
        return result


