from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs: 
            # construct the string
            array = [0] * 26
            for ch in string: 
                idx = ord(ch) - ord('a')
                array[idx] += 1
            # check if array exists already in hashmap
            if tuple(array) in hashmap:
                hashmap[tuple(array)].append(string)
            else:
                hashmap[tuple(array)] = [string]
        return [value for value in hashmap.values()]
        
