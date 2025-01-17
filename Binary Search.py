def search(nums, target):
    l = 0
    r = len(nums) - 1
    m = int((r + l) / 2)

    while l != m and r != m:
        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m
            m = int((r + l) / 2)
        elif target > nums[m]:
            l = m
            m = int((r + l) / 2)

    if nums[m] == target:
        return m
    
    try:
        if nums[m + 1] == target:
            return m + 1
    except IndexError:
        pass

    return -1
