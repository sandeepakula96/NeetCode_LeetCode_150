def twoSum(self, nums: List[int], target: int) -> List[int]: 
        h1 = dict()
        for ind, val in enumerate(nums):
            res = target - nums[ind]
            if res in h1:
                return [h1[res],ind]
            h1[val] = ind
