class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = left + (right - left)//2
            least = matrix[mid][0]
            most = matrix[mid][-1]
            if target < least:
                return findRow(left, mid-1)
            elif target > most:
                return findRow(mid+1, right)
            else:
                return mid
        
        row = findRow(0, len(matrix)-1)
        if row == -1:
            return False
        nums = matrix[row]
        def binarySearch(left: int, right: int) -> bool:
            if left > right:
                return False
            mid = left + (right - left)//2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                return binarySearch(left, mid-1)
            else:
                return binarySearch(mid+1, right)
        return binarySearch(0, len(nums)-1)
        
        