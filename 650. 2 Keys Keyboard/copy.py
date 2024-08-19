class Solution:
    def minSteps(self, n: int) -> int:
        operazioni = 0
        factor = 2
        
        # Continue until n is reduced to 1
        while n > 1:
            # Check if the current factor divides n
            while n % factor == 0:
                # Add the factor to operations (this simulates the copy-paste process)
                operazioni += factor
                # Reduce n
                n //= factor
            # Move to the next factor
            factor += 1
        
        return operazioni


def main():
    n = 3
    solution = Solution()
    print(solution.minSteps(n))

if __name__ == "__main__":
    main()