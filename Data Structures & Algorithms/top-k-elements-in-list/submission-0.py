class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has_map = {}
        count = 0
        for i in nums:
            if i not in has_map:
                has_map[i] = 0
            has_map[i] += 1
        items = list(has_map.items())
        for i in range(len(items)):
            for j in range(len(items)-i-1):
                if items[j][1] < items[j+1][1]:
                    items[j],items[j+1] = items[j+1],items[j]
        result = [items[i][0] for i in range(k)]

        return result

        
        