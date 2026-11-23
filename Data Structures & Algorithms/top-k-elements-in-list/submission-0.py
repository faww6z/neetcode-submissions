class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #traverse through list then when there is a different number restart the count
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res 

        