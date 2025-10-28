# tuple is immutable -> can be converted to a key
# list is not immutable -> cannot be converted to a key
# hashmaps cannot use ".append(xyz)"
# Dicitionary: All keys need to be initialized
# DefaultDict: All keys are already initiailized

# Key | Value

# city_map = {} #OR city_map = dict()
# cities = ["Calgary", "Vancouver", "Toronto"]
# city_map["Canada"] = [] #first initialize
# city_map["Canada"] += cities

# print(city_map)

# =====DEFAULT DICTIONARY ======
# from collections import defaultdict

# city_map = defaultdict(list)

# cities = ["Calgary", "Vancouver", "Toronto"]
# city_map["Canada"] += cities
# print(city_map)


# ======= NOTES (RETRIEVING DATA) =======
# hashmaps.keys() 
# hashmaps.values()
# hashmap.items() 

# city_map = {
#     'Canada': ['Calgary', 'Vancouver', 'Toronto',],
#     'USA': ['NYC', 'Austin', 'Seattle'],
#     'England': ['London', 'Manchester']
# }

# city_list = city_map.values()
# print(city_list, "\n")

# country_list = city_map.keys()
# print(country_list, "\n")

# all_list = city_map.items()
# print(all_list, "\n")


# ====== CODING PROBLEM =======
# Group Anagrams 
'''
Given an array of strings strs, group THE ANAGRAM together. You can return the answer in ANY ORDER
'''

from collections import defaultdict
from typing import List, Dict, Tuple


def group_anagrams(strs: List[str]) -> List[List[str]]:
    
    anagram_map = defaultdict(list)
    result = []
    
    for word in strs:
        sorted_word = tuple(sorted(word))
        anagram_map[sorted_word].append(word)
        
    for value in anagram_map.values():
        result.append(value)
    return result
    
    

if __name__ == "__main__":
    sample = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sample2 = ["nice", "mice", "ecim", "rice"]
    sample3 = []
    grouped = group_anagrams(sample)
    grouped2 = group_anagrams(sample2)
    grouped3 = group_anagrams(sample3)
    print("Input:", sample)
    print("Grouped Anagram:", grouped)
    print("Grouped Anagram:", grouped2)
    print("Grouped Anagram:", grouped3)

