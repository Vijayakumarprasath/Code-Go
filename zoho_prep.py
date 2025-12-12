#2 Sum Problem

def twoSum(nums, target):
    mp = {}
    for i, n in enumerate(nums):
        if target - n in mp:
            return [mp[target - n], i]
        mp[n] = i

#3 Valid Anagram
def isAnagram(s, t):
    return sorted(s) == sorted(t)
