class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in myMap:
                return [myMap[complement], i]
            myMap[n] = i
        return None
        