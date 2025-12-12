#2 Sum Problem

def twoSum(nums, target):
    mp = {}
    for i, n in enumerate(nums):
        if target - n in mp:
            return [mp[target - n], i]
        mp[n] = i


#3 Contains Duplicate
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
