# Given an array of strings strs, group the anagrams together. You 
# can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original 
# letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from typing import List
from collections import defaultdict

class Grouper:
    # A better solution using defaultdictm which provides a default value for 
    # non-existing key, essentially saving if-else statement
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_str = ''.join(sorted(word))
            groups[sorted_str].append(word)
        return list(groups.values())
    
    # My original solution
    # def group_anagrams(self, strs: List[str]) -> List[List[str]]:
    #     groups = {}
    #     for word in strs:
    #         sorted_str = ''.join(sorted(word))
    #         if sorted_str in groups:
    #             groups[sorted_str].append(word)
    #         else:
    #             groups[sorted_str] = [word]
    #     return list(groups.values())                 
    

gp = Grouper()    
strs = ["eat","tea","tan","ate","nat","bat"]
strs_1 = [""]
print(gp.group_anagrams(strs_1))