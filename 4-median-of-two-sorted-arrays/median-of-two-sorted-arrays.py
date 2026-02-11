class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=nums1+nums2
        num.sort()
        o=len(num)/2
        if len(num)%2!=0:
            return num[o]
        else:
            return float((num[o]+num[o-1])/2.0)