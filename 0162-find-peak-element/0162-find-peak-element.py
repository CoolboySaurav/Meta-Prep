class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        
        l, r = 1, len(nums) - 2
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid -  1] < nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1