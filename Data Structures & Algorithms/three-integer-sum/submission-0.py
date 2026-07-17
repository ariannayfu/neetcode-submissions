class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            target = -n
            
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    triplets.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
        return triplets


        