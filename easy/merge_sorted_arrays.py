class MergeSortedArrays(object):
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: None Do not return anything, modify nums1 in-place instead.
    #     """
    #     for i in range(n):
    #         nums1[m + i] = nums2[i]
    #     nums1.sort()

    # From leetcode: not using sort()
    # Sort from back! Very clever! From font will cause info lost!
    # This is why I used sort(), but from back avoids it!
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        final_pos = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[final_pos] = nums1[m]
                m -= 1
            else:
                nums1[final_pos] = nums2[n]
                n -= 1
            final_pos -= 1

        while n >= 0:
            nums1[final_pos] = nums2[n]
            n -= 1
            final_pos -= 1


msa = MergeSortedArrays()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
msa.merge(nums1, m, nums2, n)
print(nums1)
