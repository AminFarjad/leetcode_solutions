class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        li = []
        i=0
        j=0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                li.append(nums2[j])
                j+=1
            else:
                li.append(nums1[i])
                i+=1

        while i < m:
            li.append(nums1[i])
            i+=1
        while j < n:
            li.append(nums2[j])
            j+=1
        for i in range(0,m+n):
            nums1[i] = li[i]        
