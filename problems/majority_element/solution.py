class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """n=len(nums)
        if (n>=1) and (n<= 5*(10000)):
            s=n//2
            for x in range(s+1):
                m=nums[x]
                if (m>= -(10**9)) and (m<=10**9):
                    a=nums.count(m)
                    if(a>s):
                        return m  
        else:
            return 0"""
        """The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted"""
        n=len(nums)
        middle=n//2
        nums.sort()
        return nums[middle]
        
        