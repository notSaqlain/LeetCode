# ERROR: Time Limit Exceeded

# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    if prices[j] - prices[i] > max_val:
                        max_val = prices[j] - prices[i]

        return max_val
    
def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices)) # 5

if __name__ == "__main__":
    main()