class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []

        for row in matrix:
            flat.extend(row)
        
        print(flat)

        lo = 0
        hi = len(flat) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        
        return False