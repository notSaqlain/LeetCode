# Link: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = len(nums)
        for i in range(x):
            for j in range(i+1, x):
                if nums[i] + nums[j] == target:
                    return i, j


def main():
    sum = Solution()
    print(sum.twoSum([2, 7, 11, 15], 9)) # [0, 1]


if __name__ == "__main__":
    main()
