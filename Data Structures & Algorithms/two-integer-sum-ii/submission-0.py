class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r,l = 0, n-1
        while r < l:
            rem = target - numbers[r]
            if rem == numbers[l]:
                return [r+1, l+1]
            elif rem > numbers[l]:
                r += 1
            elif rem < numbers[l]:
                l -= 1
        
        return [0,0]