def containsDuplicate(self, nums):
    no_dups = set(nums)
    if len(nums) != len(no_dups):
        return True
    return False
