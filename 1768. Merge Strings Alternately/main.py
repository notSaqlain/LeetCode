# LEETCODE 75
# Link: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        lens = 0
        if len(word1) > len(word2):
            lens = len(word1)
        else:
            lens = len(word2)
        
        lists = []
        for i in range(lens):
            if i < len(word1):
                lists.append(word1[i])
            if i < len(word2):
                lists.append(word2[i])

        return ''.join(lists)

# Time: O(N)
# Space: O(N)

def main():
    word1 = "abc"
    word2 = "pqr"
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))

if __name__ == "__main__":
    main()