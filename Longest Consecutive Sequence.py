def longestConsecutive(nums):
    if nums == []:
        return 0
    nums = list(set(nums))
    nums.sort()
    current = 1
    highest = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] - 1:
            current += 1
        else:
            if current > highest:
                highest = current
            current = 1
    if current > highest:
        highest = current
    return highest
