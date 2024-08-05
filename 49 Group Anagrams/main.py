from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []

        for s in strs:
            sorted_str = tuple(sorted(s))
            anagrams[sorted_str].append(s)
            
        for value in anagrams.values():
            result.append(value)
        
        return result

def main():
  sol = Solution()
  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
  print(sol.groupAnagrams(strs))

if __name__ == "__main__":
  main()
