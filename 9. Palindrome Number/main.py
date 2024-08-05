class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)

        return temp == temp[::-1]

def main():
    pal = Solution()
    print(pal.isPalindrome(121)) # True


if __name__ == "__main__":
    main()