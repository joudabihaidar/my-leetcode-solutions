class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 is the array that we're going to merge the rest into
        # nums2 is the second array
        # m is the length of non zero elements in nums1 
        # n is the length of nums2

        # first thing we need to do is get the last index of nums1
        last=m+n-1

        # We will merge them starting with reverse order, so going backwards
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1
        
        # fill nums1 with the leftover elements in nums2
        while n>0:
            nums1[last]=nums2[n-1]
            n,last=n-1,last-1