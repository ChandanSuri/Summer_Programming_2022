class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums_map = dict()
        nums_stack = []
        total_nums = len(nums2)
        result = list()

        '''
        Firstly, we go over each and every element of the superset array...
        While going through we compare the current element in the superset array to the
        top of the stack. If it's greater than the current top of the stack, then
        that would mean that for that current top of the stack our current element 
        is the next greatest element.
        '''
        for idx in range(total_nums):
            curr_value = nums2[idx]
            '''
            We pop the elements from top of stack till the current value is greater than them.
            Or the loop will end when the stack becomes empty!
            '''
            while len(nums_stack) != 0 and curr_value > nums_stack[-1]:
                nums_map[nums_stack.pop()] = curr_value
            '''
            This runs in 2 cases:
            1. After all the elements greater than the current element are popped from the stack,
            we need to add the current value to the stack to be compared to next...
            2. Otherwise, simply the current element is added to the stack if it was less than the
            previous top of the stack.
            '''
            nums_stack.append(curr_value)

        '''
        After the above for loop has ended, we would need to add -1 signifying that no greater 
        elements exist for these elements in the stack at the moment.
        '''
        while len(nums_stack) != 0:
            nums_map[nums_stack.pop()] = -1

        '''
        As we have already saved all the next greatest elements for all elements in the superset array,
        we go over the complete list of subset array to find the next greatest elements from the hashMap.
        '''
        for num1 in nums1:
            result.append(nums_map[num1])

        return result
