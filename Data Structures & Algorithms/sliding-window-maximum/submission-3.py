from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        
        for r in range(len(nums)):
            l = r - k + 1
            while window and window[0] < l:
                window.popleft()
            
            while window and nums[window[-1]] <= nums[r]:
                window.pop()
            
            window.append(r)

            if r >= k - 1:
                result.append(nums[window[0]])
                
        
        return result