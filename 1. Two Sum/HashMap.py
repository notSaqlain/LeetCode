from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hmap:
                return [Hmap[diff], i]
            Hmap[n] = i
        return

def main():
    sum = Solution()
    print(sum.twoSum([2, 7, 11, 15], 9)) # [0, 1]


if __name__ == "__main__":
    main()
