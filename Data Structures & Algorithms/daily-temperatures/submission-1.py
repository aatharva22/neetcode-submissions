class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #Brute force approach 
        result = temperatures
        for i in range(len(temperatures)):

            right = i + 1
            while right <= len(temperatures) - 1:

                if temperatures[right] > temperatures[i]:
                    result[i] = (right - i)
                    break
                else:
                    if right == len(temperatures) - 1:
                        result[i] = 0
                    right += 1
                
                
                
        result[len(result)-1] = 0
        return result 