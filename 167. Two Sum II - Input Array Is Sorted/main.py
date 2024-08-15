# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1, r+1]
        return[l+1, r+1]

def main():
    sum = Solution()
    print(sum.twoSum([2, 7, 11, 15], 9)) # [1, 2]

if __name__ == "__main__":
    main()