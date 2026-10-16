class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range (len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             print(nums[j])
        #             return True
        # return False

        seen = set()
        for num1 in nums:
            if num1 in seen:
                print(num1)
                return True
            seen.add(num1)
        return False