class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        c=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
            else:
                if nums[i]!="_":
                    c+=1
                i+=1
        return c