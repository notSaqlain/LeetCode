# Link: https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for i in range(2, 6):
            while n%i == 0:
                n /= i

        return n==1

# Time complexity: O(logn)
# Space complexity: O(1)

def main():
    n = 14
    s = Solution()
    print(s.isUgly(n))

if __name__ == '__main__':
    main()