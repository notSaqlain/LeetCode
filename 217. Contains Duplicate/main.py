from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        for i in range(x):
            for j in range(i+1, x):
                if nums[i] == nums[j]:
                    return True
        
        return False

def main():
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.containsDuplicate(nums))

if __name__ == "__main__":
    main()    