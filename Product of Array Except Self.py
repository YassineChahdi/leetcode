# with division
def productExceptSelf(nums):
    n = 1
    lis = []
    for i in nums:
        if i == 0 and nums.count(0) == 1:
            zero = True
            continue
        n = n * i
    for i in nums:
        j = n
        if zero:
            if i != 0:
                j = 0
            else:
                j = n
        elif i == 0:
            j = 0
        else:
            j = j / i
        lis.append(int(j))      
    return lis

# without division
def productExceptSelf(nums):
    prefixes = []
    suffixes = []
    for i in range(len(nums) - 1):
        if i == 0:
            prefixes.append(nums[i])
        else:
            prefixes.append(nums[i] * prefixes[i - 1])
    prefixes.insert(0, 1)
    sufnums = nums[::-1]
    for i in range(len(sufnums) - 1):
        if i == 0:
            suffixes.append(sufnums[i])
        else:
            suffixes.append(sufnums[i] * suffixes[i - 1])
    suffixes = suffixes[::-1]
    suffixes.append(1)
    for i in range(len(nums)):
        nums[i] = prefixes[i] * suffixes[i]
    return nums
