class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(0, len(temperatures)):
            flag = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    flag = True
                    break
            if not flag:
                res.append(0)
        return res
