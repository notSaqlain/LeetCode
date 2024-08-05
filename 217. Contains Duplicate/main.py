from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        nums.sort(reverse=True)
        for i in range(x):
            if i == x - 1:
                return False
            if nums[i] == nums[i + 1]:
                return True
        return False

def main():
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))

if __name__ == "__main__":
    main()    