class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index, value in enumerate(nums):
            product1 = 1
            product2 = 1
            for i in range(0,index):
                product1 = nums[i] * product1
            for i in range(index+1,len(nums)):
                product2 = nums[i] * product2
            result.append(product1*product2)
        return result

            