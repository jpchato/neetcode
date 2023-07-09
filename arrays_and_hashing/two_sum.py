class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, number in enumerate(nums):
            if target - number in my_dict:
                return [my_dict[target  - number], index]
            my_dict[number] = index
        return []