# Source: https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        number += 1
        array = [int(digit) for digit in str(number)]
        return array


def main():
    s = Solution()
    print(s.plusOne([1,2,3])) # [1,2,4]
    print(s.plusOne([4,3,2,1])) # [4,3,2,2]
    print(s.plusOne([0])) # [1]

if __name__ == "__main__":
    main()