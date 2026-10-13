class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result  = [0] * n
        pastTemp = []

        for i in range(n):
            while pastTemp and temperatures[i] > temperatures[pastTemp[-1]]:
                old_index = pastTemp.pop()
                result[old_index] = i - old_index
            pastTemp.append(i)
        
        return result
                
