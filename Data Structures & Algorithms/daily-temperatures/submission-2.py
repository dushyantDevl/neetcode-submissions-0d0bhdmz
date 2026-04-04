class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n, res = len(temperatures), []
        for i in range(n):
            curr_temp, day_count = temperatures[i], 0
            for j in range(i+1, n):
                if curr_temp < temperatures[j]:
                    day_count += 1
                    break
                else:
                    day_count = day_count+1 if j != n-1 else 0
            res.append(day_count)
        return res

