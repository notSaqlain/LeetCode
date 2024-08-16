# Link: https://leetcode.com/problems/lemonade-change/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                else:
                    return False
            else:
                twenty += 1
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


def main():
    sol = Solution()
    bills = [5,5,5,10,20]
    print(sol.lemonadeChange(bills)) # True

if __name__ == "__main__":
    main()