class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices)) # 5

if __name__ == "__main__":
    main()