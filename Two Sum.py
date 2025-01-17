def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums.index(nums[i]), nums.index(nums[j], nums.index(nums[i]) + 1)]
