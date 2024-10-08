class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_prod, r = [1]*n, 1
        for i in range(1, n):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]
        for i in range(n - 1, -1, -1):
            left_prod[i] *= r
            r *= nums[i]
        return left_prod

        
        
        n = len(nums)
        leftProduct = [1]*n
        rightProduct = [1]*n
        leftProduct[0] = nums[0]
        rightProduct[-1] = nums[-1]
        
        for i in xrange(1, n):
            leftProduct[i] = leftProduct[i - 1]*nums[i]
        for j in xrange(n-2, -1, -1):
            rightProduct[j] = rightProduct[j + 1]*nums[j]
        
        res = [1]*n
        
        for i in xrange(n):
            a = (leftProduct[i - 1] if i > 0 else 1)
            b = (rightProduct[i + 1] if i < n - 1 else 1)
            res[i] = a*b
        
        return res