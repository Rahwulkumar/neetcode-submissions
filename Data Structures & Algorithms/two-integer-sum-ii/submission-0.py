class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keys = {}
        for index, number in enumerate(numbers):
            model = target - number

            if model in keys:
                return [keys[model]+1, index+1]
            keys[number] = index
        