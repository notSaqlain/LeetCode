# Link: https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        anagrams = defaultdict(int)
        for i in nums:
            anagrams[i] += 1 
        
        for value in anagrams.values():
            if value > 1:
                return True
        return False
        
def main():
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))

if __name__ == "__main__":
    main()    