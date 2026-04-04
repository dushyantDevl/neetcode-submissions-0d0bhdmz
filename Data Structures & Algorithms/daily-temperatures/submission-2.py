class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stk = [0]* len(temperatures), []
        for day, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                _, stackDay = stk.pop()
                res[stackDay] = (day - stackDay)
            stk.append([temp, day])
        return res