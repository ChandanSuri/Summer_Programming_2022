class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = [nums[0]]
        len_nums = len(nums)

        for idx in range(1, len_nums):
            if nums[idx] > sub[-1]:
                sub.append(nums[idx])
            else:
                # Perform binary search on sub
                leftIdx = 0
                rightIdx = len(sub) - 1

                while leftIdx < rightIdx:
                    midIdx = leftIdx + (rightIdx - leftIdx) // 2
                    if sub[midIdx] < nums[idx]:
                        leftIdx = midIdx + 1
                    else:
                        rightIdx = midIdx

                sub[rightIdx] = nums[idx]

        return len(sub)
