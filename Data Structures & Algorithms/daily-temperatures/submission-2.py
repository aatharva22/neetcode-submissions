class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        days = []

        #pattern :- monotonic stack
        for i,t in enumerate(temperatures):

            while days and t > temperatures[days[-1]] :

                idx = days.pop()
                result[idx] = i - idx

            days.append(i)
        
        return result

