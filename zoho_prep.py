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


#4 Group Anagrams
from collections import defaultdict
def groupAnagrams(strs):
    mp = defaultdict(list)
    for s in strs:
        mp[''.join(sorted(s))].append(s)
    return list(mp.values())

    
#3 Valid Anagram
def isAnagram(s, t):
    return sorted(s) == sorted(t)


#5 Top K Frequent Elements 
from collections import Counter
def topKFrequent(nums, k):
    return [x for x,_ in Counter(nums).most_common(k)]
