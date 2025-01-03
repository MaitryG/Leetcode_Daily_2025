# Problem: You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lsum = sum(nums[:1])
        rsum = sum(nums[1:])

        count = 0
        if lsum >= rsum:
            count+=1
        for i in range(1,len(nums)-1):
            lsum += nums[i]
            rsum -= nums[i]
            if lsum >= rsum:
                count+=1

        return count