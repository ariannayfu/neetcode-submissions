class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(left: int, right: int) -> int:
            if left >= right:
                return -1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                #search left
                return binary(left, mid)
            else:
                return binary(mid+1, right)
        return binary(0, len(nums))