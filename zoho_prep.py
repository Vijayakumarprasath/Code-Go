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


#5 Top K Frequent Elements 
from collections import Counter
def topKFrequent(nums, k):
    return [x for x,_ in Counter(nums).most_common(k)]
