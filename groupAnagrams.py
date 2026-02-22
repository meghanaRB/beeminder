from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            restring = ''.join(sorted(word))
            hash_map[restring].append(word)
                
        return list(hash_map.values())

            
## defaultdict is a type of dict that auto assigns values to keys that don't exist and won't throw a key error
## remember when you feel like you need a counter for string chars, you can sort them to use as keys
## since a counter is unhashable
## Time Complexity = O(n klogk) where k is the longest word
## Space Complexity = O(n)



             

            



        
