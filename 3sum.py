def threeSum(nums):
    triplets = []
    nums = sorted(nums)

    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            pass
        elif nums[i] <= 0:
            target = 0 - nums[i]
            j = i + 1
            k = -1
            while True:
                if len(nums) + k <= j:
                    break
                elif j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                elif k < - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        else:
            break

    return triplets
