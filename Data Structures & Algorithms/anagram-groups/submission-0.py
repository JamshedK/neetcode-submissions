from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        # loop through each element in a list
            # sort the element, check if already exists in hashmap, if yes, append
            # if doesn't exist, add sorted value as key, and then a new array
        
        for string in strs: 
            sorted_string = "".join(sorted(string))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]
        return [value for value in hashmap.values()]
        
