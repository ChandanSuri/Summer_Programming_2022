class Solution(object):
    def productExceptSelf(self, array):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1] * len(array)

        leftRunningProduct = 1
        for idx in range(len(array)):
            products[idx] = leftRunningProduct
            leftRunningProduct *= array[idx]

        rightRunningProduct = 1
        for idx in range(len(array) - 1, -1, -1):
            products[idx] *= rightRunningProduct
            rightRunningProduct *= array[idx]

        return products
