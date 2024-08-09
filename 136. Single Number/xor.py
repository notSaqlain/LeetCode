from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for n in nums:
            single ^= n
        return single

def main():
    s = Solution()
    print(s.singleNumber([4,1,2,1,2])) # 4

if __name__ == "__main__":
    main()