class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for value, index in enumerate(len(nums)):
            product = 1
            for i in range(len(nums)):
                if i!=index:
                    product = nums[i] * product
                    result.append(product)
        return result

            