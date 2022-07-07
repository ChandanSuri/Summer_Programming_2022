class Solution(object):
    # This is a linear time and constant space solution
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        curr_ptr_1 = m - 1
        curr_ptr_2 = n - 1

        while curr_ptr_2 >= 0 and curr_ptr_1 >= 0:
            if nums1[curr_ptr_1] > nums2[curr_ptr_2]:
                nums1[curr_ptr_1 + curr_ptr_2 + 1] = nums1[curr_ptr_1]
                curr_ptr_1 -= 1
            else:
                nums1[curr_ptr_1 + curr_ptr_2 + 1] = nums2[curr_ptr_2]
                curr_ptr_2 -= 1

        return nums1
