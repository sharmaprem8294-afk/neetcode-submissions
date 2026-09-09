class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index, value in enumerate(nums):
            product = 1
            for i in range(len(nums)):
                if i!=index:
                    product = nums[i] * product
            result.append(product)
        return result

            