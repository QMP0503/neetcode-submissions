class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        order = []
        for num, cnt in frequency.items():
            order.append([cnt, num])
        order.sort()

        res = []
        while len(res) < k:
            res.append(order.pop()[1])
    
        return res
