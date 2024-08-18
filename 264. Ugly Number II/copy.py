class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(1, n):
            next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
            ugly_numbers.append(next_ugly)
            
            if next_ugly == ugly_numbers[i2] * 2:
                i2 += 1
            if next_ugly == ugly_numbers[i3] * 3:
                i3 += 1
            if next_ugly == ugly_numbers[i5] * 5:
                i5 += 1
        
        return ugly_numbers[-1]

def main():
    n = 10
    s = Solution()
    print(s.nthUglyNumber(n))

if __name__ == '__main__':
    main()        